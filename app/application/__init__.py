from application.blueprints.routes import web
from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder='templates',
        static_url_path='',
        static_folder='static'
    )
    app.config.from_object('application.config.Config')
    
    app.register_blueprint(web, url_prefix='/')

    @app.errorhandler(404)
    def not_found(error):
        return response('404 Not Found'), 404

    @app.errorhandler(403)
    def forbidden(error):
        return response('403 Forbidden'), 403

    @app.errorhandler(400)
    def bad_request(error):
        return response('400 Bad Request'), 400

    @app.errorhandler(Exception)
    def handle_error(error):
        message = error.description if hasattr(error, 'description') else [str(x) for x in error.args]
        response = {
            'error': {
                'type': error.__class__.__name__,
                'message': message
            }
        }
        return response, error.code if hasattr(error, 'code') else 500

    return app
