import webbrowser
from flask import Flask, render_template, request, redirect, url_for
import threading
from auth import login
from auth import load_users, save_users
from flask import flash, redirect, url_for
import os
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

if __name__ == '__main__':
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/login")
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True, use_reloader=False)
