import click

from flask_alembic.cli.click import cli as alembic_cli
app.cli.add_command(alembic_cli, 'db')
