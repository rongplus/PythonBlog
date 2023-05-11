from user import *

from flask import redirect, url_for
from flask_login import logout_user
from flask_login import login_user
from flask import render_template, redirect, url_for, request
from wtforms.validators import DataRequired, EqualTo
from wtforms import StringField, PasswordField
from werkzeug.security import check_password_hash
from flask_login import UserMixin  # 引入用户基类
import uuid
from werkzeug.security import generate_password_hash
from flask import Flask
from flask_login import LoginManager
from flask_wtf import FlaskForm
from flask_login import current_user, login_required
from flask import redirect, url_for
from flask_login import logout_user
# ...
app = Flask(__name__)  # 创建 Flask 应用

app.secret_key = 'abc'  # 设置表单交互密钥

login_manager = LoginManager()  # 实例化登录管理对象
login_manager.init_app(app)  # 初始化应用
login_manager.login_view = 'login'  # 设置用户登录视图函数 endpoint


@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(user_id):
    return User.get(user_id)


# ...


class LoginForm(FlaskForm):
    """登录表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])


# ...


@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("login with ", username, password)
        user_info = get_user(username)  # 从用户数据中查找用户记录
        if user_info is None:
            emsg = "用户名或密码密码有误"
        else:
            user = User(user_info)  # 创建用户实体
            if user.verify_password(password):  # 校验密码
                login_user(user)  # 创建用户 Session
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = "用户名或密码密码有误"
        return render_template('login.html', form=form, emsg=emsg)

    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_info = get_user(user_name)  # 从用户数据中查找用户记录
        if user_info is None:
            emsg = "用户名或密码密码有误"
        else:
            user = User(user_info)  # 创建用户实体
            if user.verify_password(password):  # 校验密码
                login_user(user)  # 创建用户 Session
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = "用户名或密码密码有误"
    return render_template('login.html', form=form, emsg=emsg)


@app.route('/')  # 首页
@login_required  # 需要登录才能访问
def index():
    return render_template('index.html', username=current_user.username)


# ...


@app.route('/logout')  # 登出
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/time')  # 登出
@login_required
def getTime():
    a = {"id": 1, "time": "now"}
    return a


if __name__ == '__main__':
    app.run(debug=True)
