from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import Required, Email, Length, EqualTo, Regexp
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import User, Role
from .. import db


class LoginForm(Form):
    email = StringField("Email", validators=[
                        Required(), Length(4, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remenber_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


def get_Role():
    return Role.query

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
    Role = QuerySelectField('Role list',query_factory=get_Role,get_label='name',allow_blank=False)
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
