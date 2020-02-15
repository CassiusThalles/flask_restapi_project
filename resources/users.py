from flask_restful import Resource, reqparse
from models.users import Users as mUsers # model Users


class Users(Resource):
    def get(self):
        users = mUsers.objects().to_json()
        return users

    def post(self):
        req = reqparse.RequestParser()
        user = Users(**req).save()
        id = user.id
        return {'id': str(id)}, 200
