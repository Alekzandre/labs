from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from .models import User, Role
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        user = User(username=form.name.data)
        db.session.add(user)
        db.session.commit()
        # flash("a girl has no name")
        redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get("name"))
