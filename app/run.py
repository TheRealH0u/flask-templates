from application.main import app
from application.util import generate
from application import create_app
from application.models import db, User
from werkzeug.security import generate_password_hash
import os

basedir = os.path.abspath(os.path.dirname(__file__))

def initialize():
    database_path = os.path.normpath(f'{basedir}/database.db')
    if os.path.exists(database_path):
        return
    db.drop_all()
    db.create_all()
    
    admin = User(username='admin', email='admin@example.com', password=generate_password_hash('rockyoupass'))
    db.session.add(admin)
    user = User(username='bob', email='bob@example.com', password=generate_password_hash('password'))
    db.session.add(user)
    db.session.commit()


app = create_app()
with app.app_context():
    initialize()

app.run(host='0.0.0.0', port=5000, debug=False, use_evalex=False)
