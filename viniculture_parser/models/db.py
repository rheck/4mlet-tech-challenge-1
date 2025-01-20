from flask_sqlalchemy import SQLAlchemy

instance = SQLAlchemy()

def init_db(app):
    instance.init_app(app)
    
    with app.app_context():
        instance.create_all()
