# noinspection PyUnresolvedReferences
from config import api, app, db
from resources.HelloWorld import HelloWorld
from resources.users import Users
from resources.sellers import Sellers


api.add_resource(HelloWorld, '/')
api.add_resource(Users,'/v1/users')
api.add_resource(Sellers,'/v1/sellers')

