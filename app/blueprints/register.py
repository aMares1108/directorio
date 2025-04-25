from flask import Blueprint, redirect, render_template, url_for, request, flash, jsonify
from flask_login import login_user, login_required, current_user
from ..models.staff import Staff
from ..models.extra import Extra
from ..models.user import User
from ..extensions import db

bp = Blueprint('register', __name__, url_prefix='/register')

@bp.route('/')
@login_required
def index():
    return render_template('register.jinja', name=current_user.name)

@bp.route('/login')
def login():
    return render_template('login.jinja')

@bp.post('/login')
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or user.password!=password:
        flash('Please check your login details and try again.')
        return redirect(url_for('register.login')) # if the user doesn't exist or password is wrong, reload the page

    if login_user(user, remember=remember):
        return redirect(url_for('register.index'))
    return "Error de Login"

@bp.post('/')
@login_required
def new_staff():
    staff = Staff()
    staff.nombre = request.form.get('nombre') or None
    staff.gap = request.form.get('gap') or None
    staff.estiramiento = request.form.get('estiramiento') or None
    staff.contrato = request.form.get('contrato') or None
    staff.edad = request.form.get('edad') or None
    staff.foto = request.form.get('foto') or None
    staff.telefono = request.form.get('telefono') or None
    if staff.telefono:
        staff.telefono = staff.telefono.replace(' ','')
    staff.ocupacion = request.form.get('ocupacion') or None
    staff.residencia = request.form.get('residencia') or None

    db.session.add(staff)
    db.session.commit()
    return redirect(url_for('staff.get_only_staff', id=staff.id))
