from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from app.models.user import User
from app import login_manager

bp_login = Blueprint('bp_login', __name__)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@bp_login.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email, password = request.form['user'], request.form['password']
    user = User.from_credential(email, password)
    if user:
            login_user(user)
            return redirect('/admin')
    return render_template('login.html')


@bp_login.route('/logout')
def logout():
    logout_user()
    return redirect('/login')