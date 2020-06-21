import os
from flask import Flask
from flask_restful import Api
from resources.userreg import UserReg
from resources.loggin import UserList,login,forgot_password
from flask_jwt_extended import JWTManager
from security import  authenticate, identity
from flask_mail import *

app = Flask(__name__)
app.secret_key ='1234567890)(*&^%$#@!)'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mongo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = '1234567890)(*&^%$#@!)'
app.config['MAIL_SERVER'] = 'mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config.from_pyfile('config.cfg')

api = Api(app)
jwt = JWTManager(app)
mail = Mail(app)



api.add_resource(UserReg, '/register')
api.add_resource(login, '/loggin')
api.add_resource(UserList, '/users')
api.add_resource(forgot_password, '/forgot_password')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
    app.run(port=5000,debug = True)
