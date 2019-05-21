from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from apps.users.serializers import CreateUserRequestSchema
from apps.users.dtos import CreateUserDto


class User(HTTPMethodView):
    def get(self, request: Request) -> Union[json, NoReturn]:
        return json({'result': request})

    def post(self, request: Request) -> Union[json, NoReturn]:
        serializer = CreateUserRequestSchema().load(data=request.form)
        if serializer.errors:
            return json({'result': False})
        user_dto = CreateUserDto(**request.form)
        return json({'result': request})

    def put(self, request: Request) -> Union[json, NoReturn]:
        return json({'result': request})
