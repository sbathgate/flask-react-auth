

from sqlalchemy import exc
from flask import Blueprint
from flask import request
from flask_restx import Api
from flask_restx import fields
from flask_restx import Resource

from project import db
from project.api.models import User


users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


user = api.model('User', {
    'id': fields.Integer(readOnly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'created_date': fields.DateTime,
})

class UsersList(Resource):

    @api.expect(user, validate=True)
    def post(self):
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        response_object = {}

        user = User.query.filter_by(email=email).first()
        if user:
            response_object['message'] = 'Sorry. That email already exists.'
            return response_object, 400
        db.session.add(User(username=username, email=email))
        db.session.commit()
        response_object['message'] = f'{email} was added!'
        return response_object, 201
    
    @api.marshal_with(user, as_list=True)
    def get(self):
        return User.query.all(), 200


class Users(Resource):

    @api.marshal_with(user)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            api.abort(404, f"User {user_id} does not exist")
        return user, 200


api.add_resource(UsersList, '/users')
api.add_resource(Users, '/users/<int:user_id>')