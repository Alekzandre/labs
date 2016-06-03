from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, login_required
from . import contrat
from .models import Contrat
from .forms import ContratForm, UpdateContratForm
from .. import db


@contrat.route('/', methods=['GET', 'POST'])
@login_required
def index():
    contrats = Contrat.query.all()
    return(render_template('contrat/index.html', contrats=contrats))


@contrat.route('/contrat/<int:contrat_id>', methods=['GET', 'POST'])
@login_required
def contrat_profile(contrat_id):
    contrat = Contrat.query.get_or_404(contrat_id)
    return render_template('contrat/contrat.html', contrat=contrat)


@contrat.route('/contrat/update/<int:contrat_id>', methods=['GET', 'POST'])
@login_required
def update_contrat(contrat_id):
    contrat = Contrat.query.get_or_404(contrat_id)
    form = UpdateContratForm()
        return redirect(url_for('contrat.contrat_profile', contrat_id=contrat_id))
    return render_template('contrat/update.html', form=form)


@contrat.route('/create_contrat', methods=['GET', 'POST'])
@login_required
def create_contrat():
    form = ContratForm()
    if form.validate_on_submit():
        contrat = Contrat(slot=int(
            form.slot.data), firm_id=form.firm.data.id, project_id=str(form.project.data.id))
        db.session.add(contrat)
        return redirect(url_for('contrat.index'))
    return(render_template('contrat/create_contrat.html', form=form))
