from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from core.exceptions import ValidationErrorException
from core.decorators import is_jwt_authenticated
from apps.users.schemas import CreateUserRequestSchema, UserResponseSchema, UpdateUserRequestSchema
from apps.users.dtos import CreateUserDto, UpdateUserDto
from apps.users.interactors import CreateUserInteractor, UpdateUserInteractor, GetUserInteractor


class User(HTTPMethodView):
    # decorators = [is_jwt_authenticated]

    async def get(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        user = GetUserInteractor().execute(user_id=user_id)
        response = UserResponseSchema(user)
        return json({'data': response})

    async def put(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        validator = UpdateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        update_dto = UpdateUserDto(**validator.data)
        user = UpdateUserInteractor().execute(dto=update_dto)
        return json({'data': user})

    async def delete(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        return json({'result': True})


class UserList(HTTPMethodView):
    # decorators = [is_jwt_authenticated]

    async def get(self, request: Request) -> Union[json, NoReturn]:
        return json({"result": True})

    async def post(self, request: Request) -> Union[json, NoReturn]:
        validator = CreateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        create_dto = CreateUserDto(**validator.data)
        user = await CreateUserInteractor().execute(dto=create_dto)
        return json({'data': user})


class BlockUser(HTTPMethodView):
    async def post(self, request: Request) -> Union[json, NoReturn]:
        pass


class DeactivateUser(HTTPMethodView):
    async def post(self, request: Request) -> Union[json, NoReturn]:
        pass


class UpdateUserToAdmin(HTTPMethodView):
    async def post(self, request: Request) -> Union[json, NoReturn]:
        pass
