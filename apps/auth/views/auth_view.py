from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json


class Auth(HTTPMethodView):
    def post(self, request: Request) -> json:
        return json({'result': True}, status=200)


class Refresh(HTTPMethodView):
    def post(self, request: Request) -> json:
        return json({'result': True}, status=200)
