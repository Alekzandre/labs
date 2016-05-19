from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_required
from .forms import FirmForm
from . import firm
from .models import Firm
from .. import db


@firm.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = FirmForm()
    if form.validate_on_submit():
        firm = Firm(name=form.name.data)
        db.session.add(firm)
        flash_firm_add = "firm " + str(form.name.data) + " has been added."
        flash(flash_firm_add)
        return redirect(url_for('firm.index'))
    return(render_template('firm/index.html', form=form))
