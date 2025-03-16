   from flask import Flask
   import os

   app = Flask(__name__)

   @app.route('/')
   def hello():
       return '你好！这是我的AI换装应用测试页面'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
