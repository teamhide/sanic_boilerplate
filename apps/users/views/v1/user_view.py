from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from apps.users.serializers import CreateUserRequestSchema
from apps.users.dtos import CreateUserDto, UpdateUserDto, DeleteUserDto
from apps.users.interactors import CreateUserInteractor, UpdateUserInteractor, DeleteUserInteractor


class User(HTTPMethodView):
    def get(self, request: Request) -> Union[json, NoReturn]:
        return json({'result': request})

    def post(self, request: Request) -> Union[json, NoReturn]:
        validator = CreateUserRequestSchema().load(data=request.form)
        if validator.errors:
            return json({'result': False})
        user_dto = CreateUserDto(**validator.data)
        user = CreateUserInteractor().execute(dto=user_dto)
        return json({'result': user})

    def put(self, request: Request) -> Union[json, NoReturn]:
        return json({'result': request})
