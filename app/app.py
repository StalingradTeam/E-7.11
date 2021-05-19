import os
from flask import app, Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine

from sett import AdvertsApi, AdvertApi, AdvTagsApi, AdvCommentApi, AdvStatApi, cache

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')

app = Flask(__name__)

app.config['MONGODB_HOST'] = MONGO_HOST
app.config['MONGODB_DB'] = 'board'
app.config["CACHE_TYPE"] = 'redis'
app.config["CACHE_REDIS_HOST"] = REDIS_HOST


sett = Api(app)
db = MongoEngine(app)
cache.init_app(app)

sett.add_resource(AdvertsApi,    '/advs')
sett.add_resource(AdvertApi,     '/adv/<adv_id>')
sett.add_resource(AdvTagsApi,    '/tags/<adv_id>')
sett.add_resource(AdvCommentApi, '/comment/<adv_id>')
sett.add_resource(AdvStatApi,    '/stat/<adv_id>')

app.run(debug=True)