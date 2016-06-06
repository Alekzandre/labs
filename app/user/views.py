from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import login_required
from . import user
from .. import db
from .forms import UpdateUserForm
from ..firm.models import Firm
from ..auth.models import User, Role
import os, base64


@user.route('/', methods=['GET', 'POST'])
@login_required
def index():
    users = User.query.all()
    return render_template('user/users.html', users=users)


@user.route('/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/user.html', user=user, user_id=user_id)


@user.route('/update/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_profile(user_id):
    user = User.query.get_or_404(user_id)
    form = UpdateUserForm()
    if form.validate_on_submit():
        user.password = form.password.data
        print form.password.data
        db.session.commit()
        return redirect(url_for('user.user_profile', user_id=user_id))
    return render_template('user/update.html', form=form)


@user.route('/photo/<int:user_id>', methods=['GET'])
@login_required
def update_photo(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/photo.html', user=user, user_id=user_id)

@user.route('/photo/<int:user_id>', methods=['POST'])
@login_required
def update_photo_post(user_id):
    photo = request.form['photo']
    f = open("app/static/cdn/%d.jpg" % user_id, 'w')
    f.write(base64.b64decode(photo))
    f.close()
    return "ok"


@user.route('/delete/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.index'))
