from flask import Blueprint
from flask_restful import Api

from board.view.ping import Ping
from board.view.post import (
    Post,
    GetPosts,
    UpdatePost,
    DeletePost
)
from board.view.version import (
    VersionCheck
)

bp = Blueprint("ping", __name__, url_prefix="")
api = Api(bp)

api.add_resource(Ping, "/ping")
api.add_resource(Post, "/post")
api.add_resource(GetPosts, "/posts")
api.add_resource(UpdatePost, "/post/<int:post_id>")
api.add_resource(DeletePost, "/post/<int:post_id>")

api.add_resource(VersionCheck, "/application-info/version/<android_version>")
