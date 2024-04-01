from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Student(db.Model, UserMixin):
    firstName = db.Column(db.String, primary_key=True)
    familyName = db.Column(db.String(150))
    dob = db.Column(db.DateTime(timezone=True), default=func.now())

class Courses(db.Model):
    courseName = db.Column(db.String, primary_key=True)


