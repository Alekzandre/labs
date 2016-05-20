from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_required

from . import formation

from .. import db
from .. import intra_api
from config import Config


@formation.route('/', methods=['GET', 'POST'])
@login_required
def index():
    api = intra_api.IntraApi(Config.INTRA_API_CLIENT_ID,
                             Config.INTRA_API_CLIENT_SECRET)
    api.get_token()
    return(render_template('formation/index.html'))
