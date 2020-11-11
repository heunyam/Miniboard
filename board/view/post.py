from flask_restful import Resource
from flask import request
from board.controller.post import (
    post,
    get_posts,
    delete_post,
    modify_post
)


class GetPosts(Resource):

    def get(self):
        return get_posts()


class DeletePost(Resource):

    def delete(self, post_id):
        return delete_post(post_id)


class ModifyPost(Resource):

    def put(self):
        post_id = request.json['post_id']
        title = request.json['title']
        content = request.json['content']

        return modify_post(post_id, title, content)


class Post(Resource):

    def post(self):
        # [+] 글자 수 체크 데코레이터 만들기
        title = request.json['title']
        content = request.json['content']

        return post(title, content)
