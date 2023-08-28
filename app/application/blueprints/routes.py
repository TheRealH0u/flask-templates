from flask import Blueprint, render_template, request, session, redirect, url_for, flash, make_response
from application.models import db, User, LoginForm, RegistrationForm
from application.util import authenticated, createJWT, isAdmin
from werkzeug.security import check_password_hash, generate_password_hash

web = Blueprint('web', __name__)


@web.route('/')
def home():
    return render_template('index.html')


@web.route('/flag')
@isAdmin
def flag():
    try:
        with open('/flag.txt','r') as file:
            flag = file.read().strip()
    except Exception:
        flash("Flag couldn't be read")
        return redirect(url_for('web.home'))
    return render_template('flag.html', flag=flag)


@web.route('/logout')
def logout():
    resp = make_response(redirect(url_for('web.login')))
    resp.delete_cookie('token')
    return resp


@web.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                token = createJWT(user.username)
                resp = make_response(redirect(url_for('web.home')))
                resp.set_cookie('token', token)
                return resp
            else:
                return render_template('login.html', form=form, error=True)

    return render_template('login.html', form=form)


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        if form.password.data != form.verify.data:
            flash("Passwords don't match!")
            return redirect(url_for('web.register'))

        if not form.username.data.isalnum():
            flash("Username contains a non-alphanumeric character!")
            return redirect(url_for('web.register'))

        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email is already used!")
            return redirect(url_for('web.register'))

        hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))

    return render_template('register.html', form=form)
