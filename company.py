from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Company(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    url = StringField('url', validators=[DataRequired()])
    loc_id = StringField('loc_id')
    submit = SubmitField('Add')