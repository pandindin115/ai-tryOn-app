   import os
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_login import LoginManager

   db = SQLAlchemy()
   login_manager = LoginManager()

   def create_app(config_name=None):
       from config import config
       
       if config_name is None:
           config_name = os.environ.get('FLASK_ENV', 'default')
       
       app = Flask(__name__)
       app.config.from_object(config[config_name])
       
       db.init_app(app)
       login_manager.init_app(app)
       
       login_manager.login_view = 'auth.login'
       
       os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
       
       from app.main import main as main_blueprint
       app.register_blueprint(main_blueprint)
       
       from app.auth import auth as auth_blueprint
       app.register_blueprint(auth_blueprint, url_prefix='/auth')
       
       return app