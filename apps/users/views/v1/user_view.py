from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from core.exceptions import ValidationErrorException
from core.decorators import is_jwt_authenticated
from core.responses import response
from core.utils import TokenHelper
from apps.users.schemas import CreateUserRequestSchema, UserResponseSchema, UpdateUserRequestSchema
from apps.users.dtos import CreateUserDto, UpdateUserDto, UserListDto, UpdateUserStateDto
from apps.users.interactors import CreateUserInteractor, UpdateUserInteractor, GetUserInteractor,\
    GetUserListInteractor, BlockUserInteractor, DeactivateUserInteractor, UpdateUserToAdminInteractor


class User(HTTPMethodView):
    decorators = [is_jwt_authenticated]

    async def get(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        user_entity = await GetUserInteractor().execute(user_id=user_id)
        user = UserResponseSchema().dump(user_entity)
        return response(user)

    async def put(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        validator = UpdateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        dto = UpdateUserDto(**validator.data)
        user = await UpdateUserInteractor().execute(dto=dto)
        return response(body=user)

    async def delete(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        return response(body={'result': True})


class UserList(HTTPMethodView):
    decorators = [is_jwt_authenticated]

    async def get(self, request: Request) -> Union[json, NoReturn]:
        dto = UserListDto(offset=request.args.get('offset'), limit=request.args.get('limit'))
        users = await GetUserListInteractor().execute(dto=dto)
        return response(body=users)

    async def post(self, request: Request) -> Union[json, NoReturn]:
        validator = CreateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        dto = CreateUserDto(**validator.data)
        user = await CreateUserInteractor().execute(dto=dto)
        return response(body=user)


class BlockUser(HTTPMethodView):
    decorators = [is_jwt_authenticated]

    async def post(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        token = TokenHelper().extract_from_request(request=request)
        dto = UpdateUserStateDto(token=token, user_id=user_id)
        await BlockUserInteractor().execute(dto=dto)
        return response(body={'result': True})


class DeactivateUser(HTTPMethodView):
    async def post(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        token = TokenHelper().extract_from_request(request=request)
        dto = UpdateUserStateDto(token=token, user_id=user_id)
        await DeactivateUserInteractor().execute(dto=dto)
        return response(body={'result': True})


class UpdateUserToAdmin(HTTPMethodView):
    async def post(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        token = TokenHelper().extract_from_request(request=request)
        dto = UpdateUserStateDto(token=token, user_id=user_id)
        await UpdateUserToAdminInteractor().execute(dto=dto)
        return response(body={'result': True})
