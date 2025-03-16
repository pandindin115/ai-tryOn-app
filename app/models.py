   from datetime import datetime
   from flask_login import UserMixin
   from werkzeug.security import generate_password_hash, check_password_hash
   from app import db, login_manager

   @login_manager.user_loader
   def load_user(user_id):
       return User.query.get(int(user_id))

   class User(UserMixin, db.Model):
       __tablename__ = 'users'
       
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(64), unique=True, index=True)
       email = db.Column(db.String(120), unique=True, index=True)
       password_hash = db.Column(db.String(128))
       joined_at = db.Column(db.DateTime, default=datetime.utcnow)
       avatar_url = db.Column(db.String(256), default='static/images/default-avatar.png')
       
       garments = db.relationship('Garment', backref='owner', lazy='dynamic')
       
       @property
       def password(self):
           raise AttributeError('密码不是可读属性')
           
       @password.setter
       def password(self, password):
           self.password_hash = generate_password_hash(password)
           
       def verify_password(self, password):
           return check_password_hash(self.password_hash, password)

   class Garment(db.Model):
       __tablename__ = 'garments'
       
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(128))
       type = db.Column(db.String(32))
       gender = db.Column(db.String(16))
       image_url = db.Column(db.String(256))
       created_at = db.Column(db.DateTime, default=datetime.utcnow)
       is_favorite = db.Column(db.Boolean, default=False)
       
       user_id = db.Column(db.Integer, db.ForeignKey('users.id'))