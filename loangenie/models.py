from flask_login import UserMixin
from flask import g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from loangenie import db, login_manager
from loangenie.configure import secrete_key
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150),unique=True, nullable=False)
    organization = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # confirmEmail = db.Column(db.Boolean, default=null)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(secrete_key, expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(secrete_key)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None 
        return Users.query.get(user_id)   
    
    def __repr__(self):
        return '<email %r>' %self.email

class Candidates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidateName = db.Column(db.String(100), nullable=False)
    candidateEmail = db.Column(db.String(100), nullable=False)
    candidateTell = db.Column(db.Integer, nullable=False)
    loanAmount = db.Column(db.Integer, nullable=False)
    loanStatus = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'name': self.candidateName,
            'email': self.candidateEmail,
            'amount': self.loanAmount,
            'status': self.loanStatus
        }

    

    # def __repr__(self):
    #     return '<candidateName %r>' %self.id



