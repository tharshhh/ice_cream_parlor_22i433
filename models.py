from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    seasonal = db.Column(db.Boolean, default=False)

class Allergen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
