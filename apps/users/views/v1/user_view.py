from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from core.exceptions import ValidationErrorException
from core.decorators import is_jwt_authenticated
from core.responses import Response
from core.utils import TokenHelper
from apps.users.schemas import CreateUserRequestSchema, UserResponseSchema, UpdateUserRequestSchema,\
    LoginRequestSchema, LoginResponseSchema
from apps.users.dtos import RegisterUserDto, UpdateUserDto, UserListDto, UpdateUserStateDto,\
    LoginDto
from apps.users.interactors import RegisterUserInteractor, UpdateUserInteractor, GetUserInteractor,\
    GetUserListInteractor, BlockUserInteractor, DeactivateUserInteractor, UpdateUserToAdminInteractor,\
    LoginInteractor


class User(HTTPMethodView):
    decorators = [is_jwt_authenticated()]

    async def get(self, request: Request, user_id: int) -> Union[Response, NoReturn]:
        user_entity = await GetUserInteractor().execute(user_id=user_id)
        schema = UserResponseSchema().dump(user_entity).data
        return Response(body=schema)

    async def put(self, request: Request, user_id: int) -> Union[Response, NoReturn]:
        validator = UpdateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        dto = UpdateUserDto(**validator.data)
        user = await UpdateUserInteractor().execute(user_id=user_id, dto=dto)
        schema = UserResponseSchema().dump(user).data
        return Response(body=schema)

    async def delete(self, request: Request, user_id: int) -> Union[Response, NoReturn]:
        return Response(body={'result': True})


class UserList(HTTPMethodView):
    decorators = [is_jwt_authenticated()]

    async def get(self, request: Request) -> Union[Response, NoReturn]:
        dto = UserListDto(offset=request.args.get('offset'), limit=request.args.get('limit'))
        users = await GetUserListInteractor().execute(dto=dto)
        schema = UserResponseSchema(many=True).dump(users).data
        return Response(body=schema)

    async def post(self, request: Request) -> Union[Response, NoReturn]:
        validator = CreateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        dto = RegisterUserDto(**validator.data)
        user = await RegisterUserInteractor().execute(dto=dto)
        schema = UserResponseSchema().dump(user).data
        return Response(body=schema)


class Login(HTTPMethodView):
    decorators = [is_jwt_authenticated()]

    async def post(self, request: Request) -> Union[json, NoReturn]:
        validator = LoginRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        dto = LoginDto(**validator.data)
        token = await LoginInteractor().execute(dto=dto)
        schema = LoginResponseSchema().dump(token).data
        return Response(body=schema)


class BlockUser(HTTPMethodView):
    decorators = [is_jwt_authenticated()]

    async def post(self, request: Request, user_id: int) -> Union[Response, NoReturn]:
        token = TokenHelper.extract_from_request(request=request)
        dto = UpdateUserStateDto(token=token, user_id=user_id)
        await BlockUserInteractor().execute(dto=dto)
        return Response(body={'result': True})


class DeactivateUser(HTTPMethodView):
    decorators = [is_jwt_authenticated()]

    async def post(self, request: Request, user_id: int) -> Union[Response, NoReturn]:
        token = TokenHelper.extract_from_request(request=request)
        dto = UpdateUserStateDto(token=token, user_id=user_id)
        await DeactivateUserInteractor().execute(dto=dto)
        return Response(body={'result': True})


class UpdateUserToAdmin(HTTPMethodView):
    decorators = [is_jwt_authenticated()]

    async def post(self, request: Request, user_id: int) -> Union[Response, NoReturn]:
        token = TokenHelper.extract_from_request(request=request)
        dto = UpdateUserStateDto(token=token, user_id=user_id)
        await UpdateUserToAdminInteractor().execute(dto=dto)
        return Response(body={'result': True})
