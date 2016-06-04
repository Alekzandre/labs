from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, login_required
from . import contrat
from .models import Contrat
from ..auth.models import User
from .forms import ContratForm, UpdateContratForm
from .. import db


def registration_already_exist(user, contrat):
    for elem in user.contrat.all():
        print elem.id
        if elem.id == contrat.id:
            return 1
    return 0


@contrat.route('/', methods=['GET', 'POST'])
@login_required
def index():
    contrats = Contrat.query.all()
    return(render_template('contrat/index.html', contrats=contrats))


@contrat.route('/<int:contrat_id>', methods=['GET', 'POST'])
@login_required
def contrat_profile(contrat_id):
    contrat = Contrat.query.get_or_404(contrat_id)
    return render_template('contrat/contrat.html', contrat=contrat)


@contrat.route('/update/<int:contrat_id>', methods=['GET', 'POST'])
@login_required
def update_contrat(contrat_id):
    contrat = Contrat.query.get_or_404(contrat_id)
    form = UpdateContratForm()
    if form.validate_on_submit():
        user = form.user.data
        if registration_already_exist(user, contrat) == 1:
            flash('Le user est deja inscrits')
            return redirect(url_for('contrat.contrat_profile', contrat_id=contrat_id))
        elif contrat.used_slot < contrat.slot and registration_already_exist(user, contrat) == 0:
            contrat.used_slot += 1
            user.contrat.append(contrat)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('contrat.contrat_profile', contrat_id=contrat_id))
        else:
            flash('Le project est deja complet')
            return redirect(url_for('contrat.contrat_profile', contrat_id=contrat_id))
    return render_template('contrat/update.html', form=form, contrat=contrat)


@contrat.route('/create_contrat', methods=['GET', 'POST'])
@login_required
def create_contrat():
    form = ContratForm()
    if form.validate_on_submit():
        contrat = Contrat(slot=int(
            form.slot.data), firm_id=form.firm.data.id, project_id=str(form.project.data.id))
        db.session.add(contrat)
        return redirect(url_for('contrat.index'))
    return render_template('contrat/create_contrat.html', form=form)


@contrat.route('/remove/user/<int:user_id>/<int:contrat_id>', methods=['GET', 'POST'])
@login_required
def remove_user(user_id, contrat_id):
    contrat = Contrat.query.get_or_404(contrat_id)
    user = User.query.get_or_404(user_id)
    if registration_already_exist(user, contrat) == 1:
        user.contrat.remove(contrat)
        db.session.commit()
        contrat.used_slot -= 1
        return redirect(url_for('contrat.index'))
    flash("Ce user n'est pas inscrit a cette formation")
    return redirect(url_for('contrat.index'))
