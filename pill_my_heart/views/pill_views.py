from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect,secure_filename
from datetime import datetime
import os
from pill_my_heart import db
from pill_my_heart.forms import UserCreateForm, UserLoginForm
from pill_my_heart.models import User

bp = Blueprint('pill_search', __name__, url_prefix='/')


@bp.route('/pill_search')
def pill_search():
    return render_template('pill/pill_search.html' )

@bp.route('/uploadimg', methods=["POST"])
def imguploading():

    uploaded_file1 = request.files['file1']
    uploaded_file2 = request.files['file2']


    print(uploaded_file1)
    uploaded_file1.save(
        os.path.join(r'C:\testproject\pill_my_heart\uploadimg\\'+secure_filename(uploaded_file1.filename)))
    uploaded_file2.save(
        os.path.join(r'C:\testproject\pill_my_heart\uploadimg\\' + secure_filename(uploaded_file2.filename)))

    return render_template('pill/pill_search.html' )

@bp.route('/pill_result/', methods=('GET', 'POST'))
def result():
    return render_template('pill/pill_result.html')

@bp.route('/pill_warning/', methods=('GET', 'POST'))
def warning():
    return  render_template('pill/pill_warning.html')