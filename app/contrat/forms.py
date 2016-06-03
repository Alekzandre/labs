from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, SelectMultipleField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, NumberRange
from .. import db
from ..firm.models import Firm
from ..formation.models import Project
from ..auth.models import User


def get_Project():
    return Project.query


def get_Firm():
    return Firm.query


def get_User():
    return User.query


class ContratForm(Form):
    firm = QuerySelectField(
        'Firm list', query_factory=get_Firm, get_label='name', allow_blank=False)
    project = QuerySelectField(
        'Project list', query_factory=get_Project, get_label='name', allow_blank=False)
    slot = IntegerField('number', validators=[NumberRange(min=0, max=20)])
    submit = SubmitField("Save")


class UpdateContratForm(Form):
    users = QuerySelectField(
        'User list', query_factory=get_User, get_label='username', allow_blank=False)
    submit = SubmitField("add")
