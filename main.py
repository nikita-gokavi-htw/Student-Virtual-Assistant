import webbrowser
from flask import Flask, render_template, request, redirect, url_for
import threading
from auth import login

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login(username, password):
            return redirect(url_for('portal', username=username))
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@app.route('/portal')
def portal():
    username = request.args.get('username', 'Student')
    return render_template('portal.html', username=username)

if __name__ == '__main__':
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/login")
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
