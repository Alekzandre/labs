from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class FirmForm(Form):
    name = StringField("Firm name", validators=[Required()])
    submit = SubmitField('validate')
