# noinspection PyUnresolvedReferences
from . import app, api
from resources.HelloWorld import HelloWorld


api.add_resource(HelloWorld, '/')
