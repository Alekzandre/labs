from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_required
from . import main
from .. import db
from ..firm.models import Firm
from ..auth.models import User, Role


@main.route('/', methods=['GET', 'POST'])
def index():
	user = User.query
	return render_template('index.html', user=user)