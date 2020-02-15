from flask_restful import Resource, reqparse
from models.sellers import Sellers as mSellers # model Sellers


class Sellers(Resource):
    def get(self):
        sellers = mSellers.objects().to_json()
        return sellers

    def post(self):
        req = reqparse.RequestParser()
        seller = Sellers(**req).save()
        id = seller.id
        return {'id': str(id)}, 200