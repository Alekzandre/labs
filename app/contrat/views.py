from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, login_required
from . import contrat
from .models import Contrat
from .forms import ContratForm
from .. import db


@contrat.route('/', methods=['GET', 'POST'])
@login_required
def index():
    contrats = Contrat.query.all()
    return(render_template('contrat/index.html', contrats=contrats))


@contrat.route('/create_contrat', methods=['GET', 'POST'])
@login_required
def create_contrat():
    form = ContratForm()
    if form.validate_on_submit():
        contrat = Contrat(slot=int(form.slot.data), firm_id=form.firm.data.id)
        db.session.add(contrat)
        return redirect(url_for('contrat.index'))
    return(render_template('contrat/create_contrat.html', form=form))
