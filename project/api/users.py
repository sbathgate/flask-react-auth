

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


api.add_resource(UsersList, '/users')