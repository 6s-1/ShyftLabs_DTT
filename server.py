from flask import Flask, render_template, request, jsonify
from waitress import serve
import datetime 

app = Flask(__name__)

# Define a list to store student data
student = []

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Students page route
@app.route('/student', methods=['GET', 'POST'])
def student_page():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form.get('firstName')
        family_name = request.form.get('familyName')
        dob = request.form.get('dob')

        # Validate form data
        if not first_name or not family_name or not dob:
            return jsonify({'error': 'All fields are required.'}), 400
        try:
            dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
            today = datetime.date.today()
            if (today - dob_date).days < 3650:  # 10 years * 365 days
                return jsonify({'error': 'Student must be at least 10 years old.'}), 400
        except ValueError:
            return jsonify({'error': 'Invalid date format for Date of Birth.'}), 400

        # Add student to the list
        student.append({'first_name': first_name, 'family_name': family_name, 'dob': dob})
        return jsonify({'success': True}), 200

    return render_template('student.html', student=student)

# if __name__ == "__main__":
#     serve(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
