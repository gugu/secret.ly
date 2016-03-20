from flask import Flask
from flask.ext.log import Logging
from .secretly.db import db
from .secretly.feed import feed
from flask_cli import FlaskCLI
from flask_alembic.cli.click import cli as alembic_cli
app = Flask(__name__)
app.config['FLASK_LOG_LEVEL'] = 'DEBUG'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
FlaskCLI(app)
flask_log = Logging(app)
db.init_app(app)
app.cli.add_command(alembic_cli, 'db')


from flask_alembic import Alembic

alembic = Alembic()
alembic.init_app(app)

app.register_blueprint(feed)
