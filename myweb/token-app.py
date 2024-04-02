from flask import Flask, session, redirect, url_for
from flask_principal import Principal, Permission, RoleNeed

app = Flask(__name__)
app.secret_key = 'key111'

# Initialize Flask-Principal
principals = Principal(app)

# Define roles and permissions
admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))

# Dummy users data
users = {'admin': {'role': 'admin'}, 'editor': {'role': 'editor'}}

@app.route('/')
def index():
    return 'Home Page'

@app.route('/login/<username>')
def login(username):
    # Normally you would verify username and password here
    if username in users:
        # Store the role in the session
        session['role'] = users[username]['role']
        return redirect(url_for('admin_index' if session['role'] == 'admin' else 'editor_index'))
    return 'User not found', 404

@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin_index():
    return 'Admin Page'

@app.route('/editor')
@editor_permission.require(http_exception=403)
def editor_index():
    return 'Editor Page'

@app.route('/logout')
def logout():
    session.pop('role', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
