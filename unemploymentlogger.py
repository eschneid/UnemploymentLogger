from flask import Flask, render_template, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template
from company import Company
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@localhost/postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    title = StringField('title')
    contract_company = StringField('contract_company')
    submitted_method = StringField('submitted-method')
    outcome = StringField('outcome')
    job_number = StringField('job_number')
    date_submitted = StringField('date_submitted')
    additional_info = StringField('additional_info')

    submit = SubmitField('Add Record')


class Jobsearch(db.Model):
    __tablename__ = 'jobsearch'

    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.String(255) )
    cc = db.Column('contract_company', db.String(255) )
    submitted_method = db.Column('submitted_method', db.String(255) )
    job_number = db.Column('job_number', db.String(255) )
    date_submitted = db.Column('date_submitted', db.String(255) )
    ai = db.Column('additional_info', db.String(255) )

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('Company', backref=db.backref('js', lazy=True))

    outcome_id = db.Column(db.Integer, db.ForeignKey('outcome.id'), nullable=False)
    outcome = db.relationship('Outcome', backref=db.backref('jobsearch', lazy=True))

    def __repr__(self):
       return '<Company {}>'.format(self.name)


class Outcome(db.Model):
    __tablename__ = 'outcome'

    id = db.Column('id', db.Integer, primary_key = True)
    outcome = db.Column('outcome', db.String(255) )


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(50))

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', backref=db.backref('loc', lazy=True))

    def __repr__(self):
       return '<Company {}>'.format(self.name)


class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column('id', db.Integer, primary_key = True)
    street = db.Column(db.String(255))
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(2))
    zip = db.Column(db.Integer)


def __init__(self, name, url, loc_id):
   self.name = name
   self.url = url
   self.loc_id = loc_id

db.create_all()


@app.route('/')
@app.route('/index')
def readdb():

    return render_template('appliedto.html', result=Jobsearch.query.all())


@app.route('/addnew',  methods=['GET', 'POST'])
def addnew():
    co_name = ''
    form = Form()

    if request.method == 'POST':

        co = Company(name=request.form['name'])
        v_outcome = request.form['outcome']

        current_oc = Outcome.query.filter_by(outcome=v_outcome).first()
        flash(current_oc)
        # oc = Outcome(outcome=request.form['outcome'])
        if current_oc is None:
            oc = Outcome(outcome=v_outcome)
        else:
            oc = current_oc


        # js = Jobsearch(title=request.form['title'], outcome_id=oc.id)
        Jobsearch(title=request.form['title'], outcome=oc, company=co)
        db.session.add(oc)
        db.session.commit()

        name = request.form['name'] # company name
        title = request.form['title']
        contract_company = request.form['contract_company']
        submitted_method = request.form['submitted_method']
        outcome = request.form['outcome']  # store into outcome table; FK links to others
        job_number = request.form['job_number']
        date_submitted = request.form['date_submitted']
        additional_info = request.form['additional_info']

    else:

        if form.validate_on_submit():
            flash('Data needed')

            return redirect('/addnew')

    return render_template('addnew.html', title='Add New Job', form=form , name=co_name)

if __name__ == '__main__':
    app.run()



