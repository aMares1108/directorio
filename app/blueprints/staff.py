from flask import Blueprint, jsonify, render_template
from ..models.staff import Staff
from ..models.extra import Extra
from ..models.contact import Contact

user_bp = Blueprint('staff', __name__, url_prefix='/staff')

# @user_bp.route('/')
# def list_users():
#     users = Staff.query.all()
#     return jsonify([user.nombre for user in users])

@user_bp.route('/template')
def hello():
    return render_template('base.jinja')

@user_bp.route('/')
def person():
    results = Staff.query.order_by(Staff.prioridad.desc(), Staff.nombre).all()

    return render_template('all.jinja', results=results)

@user_bp.get('/<id>')
def get_only_staff(id):
    results = Staff.query.order_by(Staff.prioridad.desc(), Staff.nombre).all()
    person = Staff.query.get_or_404(id)
    extra = Extra.query.filter_by(staff_id=id)
    contact = Contact.query.filter_by(staff_id=id)
    return render_template('person.jinja', person=person, extra=extra, results=results, contacts=contact)
