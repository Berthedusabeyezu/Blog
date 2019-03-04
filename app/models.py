from . import db
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255)) 
    comment = db.relationship('Comment', backref='user',lazy='dynamic')
    post = db.relationship('Post' ,backref='user', lazy='dynamic')
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
 
 
    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
  

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment=db.relationship('Comment',backref='post', lazy='dynamic')
    
def save_post():
  
    db.session.add(self)
    db.session.commit() 


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

def save_comment():

    db.session.add(new_comment)
    db.session.commit()
   
         
class Quote: 
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote
