#!/usr/bin/env python3

# Standard library imports
import ipdb

# Remote library imports
from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# Local imports
from config import app, db, api
from models import User
# Views go here!


class Home(Resource):
    def get(self):
        return {"message": "welcome!"}, 200


class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # check user if it already exist in database
        try:

            # this will only run if the above doesn't return, thus the user doesn't exist
            user = User(username=username, password_hash=password)
            db.session.add(user)
            db.session.commit()
            return user.to_dict(), 201

        except IntegrityError as e:
            db.session.rollback()
            return {'error': "Username must be Unique"}, 422
        except ValueError as e:
            db.session.rollback()
            return {'error': str(e)}, 422
        # except TypeError as e:
        #     db.session.rollback()
        #     return {'error': "Username must exist"}, 422
        finally:
            db.session.close()


class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200


api.add_resource(Home, "/api")
api.add_resource(Users, "/api/users")
api.add_resource(Signup, "/api/signup")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
