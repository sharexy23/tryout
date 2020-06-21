from models.regg import UserData
from flask_restful import Resource, reqparse


class UserReg(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('date_of_birth',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('username',
                        type=str ,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str ,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('email',
                        type=str ,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    def post(self):
        data = UserReg.parser.parse_args()
        if UserData.find_by_username(data['username']):
            return {'message': 'that username exists change it or die'}
        user = UserData(data['name'] , data['date_of_birth'] , data['username'] , data['password'], data['email'])
        try:
            user.save_to_db()
        except:
            return {'message': 'internal server error'}
        return {'message': 'you have registered'}
