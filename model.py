from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60), nullable=False)
    user_password = db.Column(db.String(30), nullable=False)
    user_nickname = db.Column(db.String(50))
    user_email = db.Column(db.String(30), nullable=False)