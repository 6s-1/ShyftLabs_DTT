from os import path
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gvfvsvf'
    app.config["SQLALCHEMY_DATABASE_URI"]= f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .models import Student, Courses

    create_database(app)
   

    # Homepage route
    @app.route('/')
    def index():
        return render_template('index.html')

    # Students page route
    @app.route('/student', methods=['GET', 'POST'])
    def student_page():
        if request.method == 'POST':
            first_name = request.form.get('firstName')
            family_name = request.form.get('familyName')
            dob = request.form.get('dob')

            if not first_name or not family_name or not dob:
                return jsonify({'error': 'All fields are required.'}), 400

            try:
                dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
                today = datetime.date.today()
                if (today - dob_date).days < 3650:
                    return jsonify({'error': 'Student must be at least 10 years old.'}), 400
            except ValueError:
                return jsonify({'error': 'Invalid date format for Date of Birth.'}), 400

            new_student = Student(firstName=first_name, familyName=family_name, dob=dob_date)
            db.session.add(new_student)
            db.session.commit()

            return jsonify({'success': True}), 200

        students = Student.query.all()
        return render_template('student.html', students=students)

    @app.route('/courses', methods=['GET', 'POST'])
    def courses_page():
        if request.method == 'POST':
            course_name = request.form.get('CourseName')
            if not course_name:
                return jsonify({'error': 'All fields are required.'}), 400

            # Create and adding course to the database
            new_course = Courses(courseName=course_name)
            db.session.add(new_course)
            db.session.commit()

        courses = Courses.query.all()
        return render_template('courses.html', courses=courses)
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
         with app.app_context():
            if not path.exists('website/' + DB_NAME):
                db.create_all()
            print("Created Database!")

