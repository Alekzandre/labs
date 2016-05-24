from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, FileField, PasswordField
from wtforms.validators import Required, EqualTo
from wtforms import validators
import re


class NameForm(Form):
    name = StringField("name please", validators=[Required()])
    submit = SubmitField('got it')

class PicUploadForm(Form):
    image = FileField(u'Image File')
    submit = SubmitField('got it')

class UpdateUserForm(Form):
    password = PasswordField('New Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm New Password', validators=[Required()])
    submit = SubmitField('got it')
