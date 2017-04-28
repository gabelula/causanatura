from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Titular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True)
    rnpa = db.Column(db.String(12), unique=True)
    rfc = db.Column(db.String(12), unique=True)

    def __init__(self, nombre, rnpa, rfc):
        self.nombre = nombre
        self.rnpa = rnpa

    def __repr__(self):
        return '<User %r>' % self.username
