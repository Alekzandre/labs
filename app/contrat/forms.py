from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, NumberRange
from .. import db
from ..firm.models import Firm


def get_Firm():
    return Firm.query


class ContratForm(Form):
    firm = QuerySelectField(
        'Firm list', query_factory=get_Firm, get_label='name', allow_blank=False)
    slot = IntegerField('number', validators=[NumberRange(min=0, max=20)])
    submit = SubmitField("Save")
