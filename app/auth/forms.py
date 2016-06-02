from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import Required, Email, Length, EqualTo, Regexp
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import User, Role
from ..firm.models import Firm
from .. import db


class LoginForm(Form):
    email = StringField("Email", validators=[
                        Required(), Length(4, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remenber_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


def get_Role():
    return Role.query

def get_Firm():
	return Firm.query

class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    role = QuerySelectField('Role list',query_factory=get_Role,get_label='name',allow_blank=False)
    firm = QuerySelectField('Firm list',query_factory=get_Firm,get_label='name',allow_blank=False)
    mobile = StringField('Phone Number', validators=[Required(), Length(10), Regexp('^[0-9]*$')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
