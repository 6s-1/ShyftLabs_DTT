from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150), nullable=False)
    familyName = db.Column(db.String(150), nullable=False)
    dob = db.Column(db.DateTime(timezone=True), default=func.now())

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(150), nullable=False)


