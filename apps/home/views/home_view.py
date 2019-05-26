from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json


class Home(HTTPMethodView):
    def get(self, request: Request) -> json:
        return json({'result': True}, status=200)
