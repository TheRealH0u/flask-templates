from flask import Blueprint, render_template, request, session, redirect, url_for, flash, make_response

web = Blueprint('web', __name__)


@web.route('/')
def home():
    return render_template('index.html')