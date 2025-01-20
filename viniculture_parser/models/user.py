from viniculture_parser.models import db

# Modelo de Usuário
class User(db.instance.Model):
    id = db.instance.Column(db.instance.Integer, primary_key=True)
    username = db.instance.Column(db.instance.String(80), unique=True, nullable=False)
    password = db.instance.Column(db.instance.String(200), nullable=False)
