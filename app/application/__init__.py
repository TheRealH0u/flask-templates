from flask import Flask
from application.models import db


def create_app():
    app = Flask(
        __name__,
        template_folder='templates',
        static_url_path='',
        static_folder='static'
    )
    app.config.from_object('application.config.Config')

    db.init_app(app)

    from application.blueprints.routes import web
    app.register_blueprint(web, url_prefix='/')

    return app
