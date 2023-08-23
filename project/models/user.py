from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import unique
from project.extensions import db , login_manager
import datetime


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(250))
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, email, username, password, confirmed, admin=False, confirmed_on=None):
        self.email = email
        self.username = username
        self.password = self.set_password(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def check_confirmed(self):
        return self.confirmed
    
    def set_confirmed(self, confirmed=True):
        self.confirmed= confirmed
    
@login_manager.user_loader
def load_user(id):
    return UserModel.query.get(int(id))