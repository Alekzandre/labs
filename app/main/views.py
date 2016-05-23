from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import login_required
from . import main
from .. import db
from .forms import PicUploadForm
from ..firm.models import Firm
from ..auth.models import User, Role
import os
from werkzeug import secure_filename


@main.route('/users', methods=['GET', 'POST'])
@login_required
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@main.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user(user_id):
    user = User.query.get(user_id)
    return render_template('main/user.html', user=user)


@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    user = User.query.filter_by(id=session['user_id']).first()
    completed = user.username + '.png'
    form = PicUploadForm()
    if form.validate_on_submit():
        file = form.image.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('/Users/jacob/LABS/labs/cdn', completed))
            return redirect(url_for('main.index'))
    return render_template('main/upload.html', form=form)
