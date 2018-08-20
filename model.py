from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(use_native_unicode='utf8')


class Good(db.Model):
    __tablename__ = 'good'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    good_pic_url = db.Column(db.String(20), nullable=False)
    good_price = db.Column(db.Integer, nullable=False)
    good_name = db.Column(db.String(20), nullable=False)



class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    num = db.Column(db.Integer, nullable=False)
    good_id = db.Column(db.Integer, db.ForeignKey('good.id'))
    time = db.Column(db.Date, default=datetime.date.today())
    good_info = db.relationship('Good', backref=db.backref('orders'))