   import os
   from datetime import timedelta

   class Config:
       SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
       SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
       if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
           SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)
       SQLALCHEMY_TRACK_MODIFICATIONS = False
       UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'uploads'
       MAX_CONTENT_LENGTH = 16 * 1024 * 1024

   class DevelopmentConfig(Config):
       DEBUG = True

   class ProductionConfig(Config):
       pass

   config = {
       'development': DevelopmentConfig,
       'production': ProductionConfig,
       'default': DevelopmentConfig
   }