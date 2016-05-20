from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_required
from . import main
from .. import db
from ..firm.models import Firm
from ..auth.models import User, Role


@main.route('/users', methods=['GET', 'POST'])
@login_required
def index():
	user = User.query
	return render_template('index.html', user=user)


@main.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user(user_id):
	user = User.query.get(user_id)
	return render_template('main/user.html', user=user)