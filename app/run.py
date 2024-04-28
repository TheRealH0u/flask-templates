from application.main import app
from application.util import generate
from application import create_app
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = create_app()

app.run(host='0.0.0.0', port=5000, debug=False, use_evalex=False)
