from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(use_native_unicode='utf8')


class Good(db.Model):
    good_id = db.Column(db.Integer, primary_key=True)
    good_pic_url = db.Column(db.String(20), nullable=False)
    good_price = db.Column(db.Integer, nullable=False)
    good_name = db.Column(db.String(20), nullable=False)



class All(db.Model):
    all_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    good_num = db.Column(db.Integer, nullable=False)
    good_id = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Date, default=datetime.date.today())