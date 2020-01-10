from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QRForm(FlaskForm):
    qrgen = StringField('TEXTSOMGÖRSTILLQR', validators=[DataRequired()])
    submit = SubmitField('MAKE')
