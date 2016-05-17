from flask import render_template, session, redirect, url_for, flash
# from .forms import NameForm
from . import auth
from .models import User
from .. import db

@auth.route('/login',methods=['GET', 'POST'])
def index():
	return(render_template('auth/login.html'))