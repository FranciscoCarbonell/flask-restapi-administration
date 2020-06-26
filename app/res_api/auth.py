from flask import g
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token
from flask_restplus import Resource
from app import api
from app.models.user import User

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def auth_verify(email, password):
    user = User.from_credential(email, password)
    if user:
        g.user_id = user.id
        return True
    return False


@api.route('/auth')
class Auth(Resource):
    @basic_auth.login_required
    def get(self):
        return {'access_token':create_access_token(identity=g.user_id)}