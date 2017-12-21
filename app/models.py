from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))



class Sender(db,Model):
    """class that sends message to a receiver"""
    __tablename__ = "sender"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(user.id))

class Recepient(db,Model):
    """class that receives message from sender"""
    __tablename__ = "sender"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recepient_id = db.Column(db.Integer, db.ForeignKey(user.id))


class DirectMessage(db.Model):
    """class to handle direct messaging between users"""
      __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender = db.Column(db.Integer,db.ForeignKey('users.id'))
    recepient = db.Column(db.Integer,db.ForeignKey('recepient.id'))
    message = db,Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'
