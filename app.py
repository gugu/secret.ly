from flask import Flask, session, request
from flask.ext.log import Logging
from flask_cli import FlaskCLI
from flask_alembic.cli.click import cli as alembic_cli
from flask_alembic import Alembic

from .secretly.db import db
from .secretly.feed import feed
from .secretly.auth import auth


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['FLASK_LOG_LEVEL'] = 'DEBUG'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'eps-Oyb-Toj-fI'

FlaskCLI(app)
flask_log = Logging(app)
db.init_app(app)
app.cli.add_command(alembic_cli, 'db')

alembic = Alembic()
alembic.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(feed)


@app.before_request
def before_request():
    from .secretly.models.user import User
    if session.get('user_id'):
        request.user = User.query.get(session['user_id'])
