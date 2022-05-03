from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Notes(db.Model):
    nid=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(1000),nullable=False)
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.uid'))     #use lowercase in ForeignKey

class Reminder():
    pass

class User(db.Model,UserMixin):
    uid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(200),unique=True)
    password=db.Column(db.String(100),nullable=False)
    notes=db.relationship('Notes')    #Use Exact name in Relationship

    def get_id(self):
           return (self.uid)