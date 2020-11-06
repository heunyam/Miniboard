from flask_restful import Resource
from flask import request
from board.controller.post import (
    post,
    get_posts
)


class GetPosts(Resource):

    def get(self):

        return get_posts()


class DeletePost(Resource):

    def delete(self, post_id):
        pass


class UpdatePost(Resource):

    def update(self):
        pass


class Post(Resource):

    def post(self):
        # [?] 글자수를 체크 해줘야 할까?
        title = request.json['title']
        content = request.json['content']

        return post(title, content)