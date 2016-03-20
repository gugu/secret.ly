from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .models.feed import Record

feed = Blueprint('feed', __name__, template_folder='templates')


@feed.route('/')
def show():
    return render_template('feed.html', dict(feed=Record.query.all()[0:10]))
