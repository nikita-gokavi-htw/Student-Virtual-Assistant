import webbrowser
from flask import Flask, render_template, request, redirect, url_for
import threading
from auth import login
from auth import load_users, save_users
from flask import flash, redirect, url_for
import os
from models.university import University
from models.person import Student, Teacher
from models.course import Course
# Test user data
users = load_users()
users["new_student"] = {"username": "new_student", "password": "secure123"}
save_users(users)

# Verify it's saved
print("✅ Current Users:", load_users())

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        if username in users and users[username]['password'] == password:
            return redirect(url_for('portal', username=username))
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@app.route('/portal')
def portal():
    username = request.args.get('username', 'Student')
    return render_template('portal.html', username=username)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simulated user store
        users = load_users()

        if username in users:
            return render_template('signup.html', error="Username already exists.")

        users[username] = {'password': password}
        save_users(users)

        # Flash success message
        flash("Account created successfully! Please login.", "success")

        # Redirect to login page
        return redirect(url_for('login_page'))

    return render_template('signup.html')

@app.route('/students', methods=['GET', 'POST'])
def handle_students():
    if request.method == 'POST':
        data = request.form  # Get data from form
        student = Student(
            name=data['name'],
            contact_info=data['contact_info']
        )
        student_id = university.add_student(student)
        flash(f"Student {student.name} created successfully!", "success")
        return redirect(url_for('portal'))

    # For GET request, list all students
    return render_template('students.html', students=university.students)

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Get details of a student by ID"""
    student = university.get_student_by_id(student_id)
    return render_template('student_detail.html', student=student)

@app.route('/courses', methods=['GET', 'POST'])
def handle_courses():
    if request.method == 'POST':
        data = request.form  # Get course data from form
        course = Course(
            course_name=data['course_name'],
            course_code=data['course_code']
        )
        university.add_course(course)
        flash(f"Course {course.course_name} added successfully!", "success")
        return redirect(url_for('portal'))

    # For GET request, list all courses
    return render_template('courses.html', courses=university.courses)

@app.route('/students/list')
def list_students():
    students_data = [student.to_dict() for student in university.students.values()]
    return render_template('students.html', students=students_data)

@app.route('/courses/list')
def list_courses():
    courses_data = [course.to_dict() for course in university.courses.values()]
    return render_template('courses.html', courses=courses_data)

university = University()
# Sample data
university.add_student(Student(name="Alice", contact_info={"email": "alice@mail.com", "phone": "12345"}))
university.add_student(Student(name="Bob", contact_info={"email": "bob@mail.com", "phone": "67890"}))

university.add_course(Course(course_id="CS101", name="Intro to CS", description="Basics of computer science"))
university.add_course(Course(course_id="MATH101", name="Calculus", description="Introduction to Calculus"))

if __name__ == '__main__':
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/login")
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True, use_reloader=False)

