from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from . import auth
from .models import User, Role
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.data['email']).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remenber_me.data)
            return redirect(url_for('main.index'))
        flash('invalid username or password')
    return(render_template('auth/login.html', form=form))


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    # flash('You haven been logged out')
    return(render_template('goodbye.html'))


@auth.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	print form.role.data.id
        print form.firm.data.id
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data,
                    role_id=form.role.data.id,
                    firm_id=form.firm.data.id
                    )
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.register'))
    return render_template('auth/register.html', form=form)
