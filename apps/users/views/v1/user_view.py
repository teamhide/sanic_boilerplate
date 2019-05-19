from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json


class User(HTTPMethodView):
    def get(self, request: Request) -> Union[json, NoReturn]:
        return json({'result': request})

    def post(self, request: Request) -> Union[json, NoReturn]:
        return json({'result': request})

    def put(self, request: Request) -> Union[json, NoReturn]:
        return json({'result': request})
