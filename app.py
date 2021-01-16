# Name:  
# Student Id : 

import flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String , Float
import os
from flask_marshmallow import Marshmallow

# flask application object
app = flask.Flask(__name__)

#app.config["DEBUG"] = True

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'app1.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/mcit/cst-students/all',methods=['GET'])
def student_all():
    student_list = Student1.query.all()
    result =  student_schema.dump(student_list)
    return jsonify(result)

class Student1(db.Model):
    __tablename__ = 'students'
    ID = Column(Integer ,primary_key=True)
    Name = Column(String)
    Branch = Column(String)
    College = Column(String)
    Batch = Column(String)
    Program = Column(String)
    Course =  Column(String)
    First_Language = Column(String)


class StudentSchema1(ma.Schema):
    class Meta:
        fields = ('ID','Name','Branch','College','Batch','Program','Course','First_Language')



student_schema = StudentSchema1()
student_schema = StudentSchema1(many=True)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created')
    
@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Databse Dropped')

@app.cli.command('db_seed')
def db_seed():
    Abhishek = Student1(Name = 'Abhishek Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Karandeep = Student1(Name = 'Karandeep Bishnoi',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'CPP')
    Harjant = Student1(Name = 'Harjant Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Java')
    Harmandeep = Student1(Name = 'Harmandeep Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Kamaljeet = Student1(Name = 'Kamaljeet Kaur',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'CPP')
    Imran = Student1(Name = 'Imran Khan',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Java')
    Kulveer = Student1(Name = 'Kulveer Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Harsh = Student1(Name = 'Harsh Pahwa',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Divyaben = Student1(Name = 'Divyaben Dipak Kumar',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Python')
    Nishaben = Student1(Name = 'ANishaben Vishubhai',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Rajinder = Student1(Name = 'Rajinder Kumar',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Python')
    Rakshat = Student1(Name = 'Rakshat Kumar',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Anubhav = Student1(Name = 'Anubhav Sachdeva',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Java')
    Anmol = Student1(Name = 'Anmol Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'CPP')
    Drashya = Student1(Name = 'Drashya Nipunkumar',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Python')
    Karan = Student1(Name = 'Karan Sharma',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Papinder = Student1(Name = 'Papinder Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Jasmeet = Student1(Name = 'Jasmeet Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Java')
    Manpreet = Student1(Name = 'Manpreet Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'C')
    Tanvir = Student1(Name = 'Tanvir Singh',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Python')
    Anchalpreet = Student1(Name = 'Anchalpreet Kaur',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Java')
    Premsai = Student1(Name = 'Premsai Tummati',
                      Branch = 'CS',
                      College = 'MCIT',
                      Batch = 'A',
                      Program = 'CST',
                      Course = 'Advance Programming',
                      First_Language = 'Python')      

    db.session.add(Abhishek)
    db.session.add(Karandeep)
    db.session.add(Harjant)
    db.session.add(Harmandeep)
    db.session.add(Kamaljeet)
    db.session.add(Imran)
    db.session.add(Kulveer)
    db.session.add(Harsh)
    db.session.add(Divyaben)
    db.session.add(Nishaben)
    db.session.add(Rajinder)
    db.session.add(Rakshat)
    db.session.add(Anubhav)
    db.session.add(Anmol)
    db.session.add(Drashya)
    db.session.add(Karan)
    db.session.add(Papinder)
    db.session.add(Jasmeet)
    db.session.add(Manpreet)
    db.session.add(Tanvir)
    db.session.add(Anchalpreet)
    db.session.add(Premsai)
      
    db.session.commit()
    print('Database seeded')

app.run()