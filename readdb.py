from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template


app = Flask(__name__)


t = Template("Hello {{ something }}!")

t.render(something="World")



# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/postgres'

db = SQLAlchemy(app)
class company(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   url = db.Column(db.String(50))
   loc_id = db.Column(db.Integer)


def __init__(self, name, url, loc_id):
   self.name = name
   self.url = url
   self.loc_id = loc_id

db.create_all()



@app.route('/')
def readdb():


    # import psycopg2.extras

    # con = psycopg2.connect(host='127.0.0.1', port='5432', user='postgres', password='1234', dbname='postgres')
    # print("Connected to postgres source DB!!!")

    # cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # cur.itersize = 10000

    sql = '''select p.fname, p.lname, c.name, js.title, js.contract_company, l.city, js.submitted_method, js.outcome, js.job_number,
       js.date_submitted, js.additional_info
from person p,
     company c,
     location l,
     jobsearch js
where p.id = js.person_applying
and js.company_id = c.id
and c.loc_id = l.id
'''


    # cur.execute(sql,)
    # rows = cur.fetchone()
    # str = rows['fname'] + ' ' + rows['lname'] + ' ' + rows['name'] +  ' ' + rows['title']

    # str = ''
    # for p in rows:
    #    #str = str + p['fname'] + ' ' + p['lname']
    #    str = str + p[0] + ' ' + p[1]
    #    rows = cur.fetchone()

    # return 'Hello World!'
    # return str

    # dict = {'phy': 50, 'che': 60, 'maths': 70}

    # return render_template('appliedto.html', result=rows)
    return render_template('appliedto.html', result=company.query.all())

if __name__ == '__main__':
    app.run()



