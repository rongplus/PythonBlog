from flask import Flask

from flask import Flask, jsonify, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired
from flask import Flask, redirect, url_for, render_template, request, flash, session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! From me'


incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return 'Get a post', 204


class LoginForm(FlaskForm):
    username = StringField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Password', validators=[DataRequired()])


@app.route('/index')
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return 'hello'


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd == '123':  # 这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码输入错误')


if __name__ == "__main__":
    app.secret_key = 'QWERTYUIOP'
    app.run(host='0.0.0.0', port="5001")
