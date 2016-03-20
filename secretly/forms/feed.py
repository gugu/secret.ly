from flask_wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class PostForm(Form):
    text = StringField('Text', validators=[DataRequired()], widget=TextArea())


class CommentForm(Form):
    text = StringField('Text', validators=[DataRequired()], widget=TextArea())
