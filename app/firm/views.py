from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_required
from .forms import FirmForm
from . import firm
from .models import Firm
from ..auth.models import User, Role
from ..contrat.models import Contrat
from .. import db


@firm.route('/', methods=['GET', 'POST'])
@login_required
def index():
    firms = Firm.query.all()
    users = User.query.all()
    return render_template('firm/index.html', firms=firms, users=users)

@firm.route('/<int:firm_id>', methods=['GET', 'POST'])
@login_required
def firm_profile(firm_id):
    firm = Firm.query.get_or_404(firm_id)
    users = User.query.filter_by(firm_id=firm.id).all()
    contrats = Contrat.query.filter_by(firm_id=firm.id).all()
    return render_template('firm/firm.html', firm=firm, users=users, contrats=contrats)

@firm.route('/add_firm', methods=['GET', 'POST'])
@login_required
def add_firm():
    form = FirmForm()
    if form.validate_on_submit():
        firm = Firm(name=form.name.data)
        db.session.add(firm)
        flash_firm_add = "firm " + str(form.name.data) + " has been added."
        flash(flash_firm_add)
        return redirect(url_for('firm.index'))
    return(render_template('firm/add_firm.html', form=form))

@firm.route('/delete/<int:firm_id>', methods=['GET', 'POST'])
@login_required
def delete_firm(firm_id):
    firm = Firm.query.get_or_404(firm_id)
    db.session.delete(firm)
    db.session.commit()
    return redirect(url_for('firm.index'))
