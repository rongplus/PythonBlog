from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('home'))
    return 'Invalid credentials'

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return f'Welcome {session["username"]}! You are logged in.'

@app.route('/status')
def status():
    if session.get('logged_in'):
        return f'User {session["username"]} is currently logged in.'
    return 'No user is currently logged in.'

if __name__ == '__main__':
    app.run(debug=True)
