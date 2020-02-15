from flask_mongoengine import MongoEngine
from routes import app


db = MongoEngine()

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/flask_app'
}

db.init_app(app)
