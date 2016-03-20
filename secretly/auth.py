from flask import Blueprint, render_template
from .models.user import User
from .forms.auth import LoginForm, SignupForm
from flask import session, redirect
from crypt import crypt
from .db import db
from .utils import random_string

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        session['user_id'] = user.id
        return redirect('/')
    return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        salt = random_string(8)
        user = User(email=form.email.data, password=crypt(form.password.data, salt), salt=salt)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        return redirect('/')
    return render_template('signup.html', form=form)
