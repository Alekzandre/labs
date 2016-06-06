from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_required

from . import formation
from .models import Project
from .. import db
from .. import intra_api
from config import Config


@formation.route('/', methods=['GET', 'POST'])
@login_required
def index():
    projects = Project.query.all()
    # api = intra_api.IntraApi(Config.INTRA_API_CLIENT_ID,
    #                          Config.INTRA_API_CLIENT_SECRET)
    # projects = api.get_projects()
    # todo populate db
    # project = Project(id_intra=int("1"), name="fuck you", desc="ta mere")
    # db.session.add(project)
    for p in projects:
        pass
    #     print p[0], p[1], p[2]
    #     project = Project(id_intra=int(p[0]), name=p[1], desc="")
    #     db.session.add(project)
    return(render_template('formation/index.html', projects=projects))

# @formation.route('/create_user', methods=['GET', 'POST'])
# @login_required
# def create_user():
#     api = intra_api.IntraApi(Config.INTRA_API_CLIENT_ID,
#                              Config.INTRA_API_CLIENT_SECRET)
#     new_user = api.create_User('alex@alex.org', 'alex', 'carayon')
#     print new_user.response
#     return redirect(url_for('formation.index'))
