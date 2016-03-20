from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from ..models.user import User

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_email(self, email):
        if not User.query.filter_by(email=email.data).count():
            raise ValidationError('User not found')

class SignupForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).count():
            raise ValidationError('User already exists')
