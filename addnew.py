from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('name')
    title = StringField('title')
    contract_company = StringField('contract_company')
    submitted_method = StringField('submitted-method')
    outcome = StringField('outcome')
    job_number = StringField('job_number')
    date_submitted = StringField('date_submitted')
    additional_info = StringField('additional_info')

    submit = SubmitField('Sign In')
