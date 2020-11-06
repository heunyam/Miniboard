from flask import Blueprint
from flask_restful import Api

from board.view.ping import Ping
from board.view.post import Post

bp = Blueprint("ping", __name__, url_prefix="")
api = Api(bp)

api.add_resource(Ping, "/ping")
api.add_resource(Post, '/post')
