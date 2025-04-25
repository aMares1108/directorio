from ..extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    name = db.Column(db.String(32))
