from flask_restful import Resource
from flask import request
from board.controller.version import check_recently_version

# 클라이언트의 앱 버전이 넘어온다
# db 내의 버전과 비교해서
# is_latest: true or false 반환
class VersionCheck(Resource):

    def get(self, android_version):
        android_version
        return check_recently_version(android_version)
