from ..extensions import db

class Extra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    valor = db.Column(db.String(64), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))