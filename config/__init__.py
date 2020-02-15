from .dbconnect import app, db
from flask_restful import Api

api = Api(app)