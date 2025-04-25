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
        return redirect(request.args.get('next', url_for('register.index')))
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
    staff.ocupacion = request.form.get('ocupacion') or None
    staff.residencia = request.form.get('residencia') or None

    db.session.add(staff)
    db.session.commit()
    return redirect(url_for('staff.get_only_staff', id=staff.id))

@bp.route('/<id>')
@login_required
def update_view(id):
    staff = Staff.query.get_or_404(id)
    return render_template('register.jinja', name=current_user.name, staff=staff)

@bp.post('/<id>')
@login_required
def update(id):
    staff = Staff.query.get_or_404(id)
    staff.nombre = request.form.get('nombre') or None
    staff.gap = request.form.get('gap') or None
    staff.estiramiento = request.form.get('estiramiento') or None
    staff.contrato = request.form.get('contrato') or None
    staff.edad = request.form.get('edad') or None
    staff.foto = request.form.get('foto') or None
    staff.telefono = request.form.get('telefono') or None
    staff.ocupacion = request.form.get('ocupacion') or None
    staff.residencia = request.form.get('residencia') or None

    db.session.add(staff)
    db.session.commit()
    return redirect(url_for('staff.get_only_staff', id=staff.id))

@bp.route('/extra/<id>')
@login_required
def extra_view(id):
    staff = Staff.query.get_or_404(id)
    return render_template('register_extra.jinja', name=current_user.name, staff=staff)

@bp.post('/extra/<id>')
@login_required
def add_extra(id):
    extra = Extra()
    extra.nombre = request.form.get('nombre')
    extra.valor = request.form.get('valor')
    extra.staff_id = id

    db.session.add(extra)
    db.session.commit()
    flash(f'Extra {extra.nombre} agregado correctamente.')
    return redirect(url_for('register.extra_view', id=id))
