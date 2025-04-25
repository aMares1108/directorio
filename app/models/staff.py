from ..extensions import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), unique=True, nullable=False)
    gap = db.Column(db.String(64))
    estiramiento = db.Column(db.String(64))
    contrato = db.Column(db.String(64))
    edad = db.Column(db.Integer)
    foto = db.Column(db.Text, unique=True)
    telefono = db.Column(db.String(10))
    ocupacion = db.Column(db.String(32))
    residencia = db.Column(db.Text)
    prioridad = db.Column(db.Integer, default=0, nullable=False)
    extras = db.relationship('Extra', backref='staff')
