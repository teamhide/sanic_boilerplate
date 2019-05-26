from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from core.exceptions import ValidationErrorException
from core.decorators import is_jwt_authenticated
from core.utils import TokenExtractor
from apps.users.schemas import CreateUserRequestSchema, UserResponseSchema, UpdateUserRequestSchema,\
    BlockUserRequestSchema
from apps.users.dtos import CreateUserDto, UpdateUserDto, UserListDto, BlockUserDto
from apps.users.interactors import CreateUserInteractor, UpdateUserInteractor, GetUserInteractor, GetUserListInteractor,\
    BlockUserInteractor


class User(HTTPMethodView):
    decorators = [is_jwt_authenticated]

    async def get(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        user = await GetUserInteractor().execute(user_id=user_id)
        response = UserResponseSchema(user)
        return json({'data': response})

    async def put(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        validator = UpdateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        update_dto = UpdateUserDto(**validator.data)
        user = await UpdateUserInteractor().execute(dto=update_dto)
        return json({'data': user})

    async def delete(self, request: Request, user_id: int) -> Union[json, NoReturn]:
        return json({'result': True})


class UserList(HTTPMethodView):
    decorators = [is_jwt_authenticated]

    async def get(self, request: Request) -> Union[json, NoReturn]:
        dto = UserListDto(offset=request.args.get('offset'), limit=request.args.get('limit'))
        users = await GetUserListInteractor().execute(dto=dto)
        return json({'data': users})

    async def post(self, request: Request) -> Union[json, NoReturn]:
        validator = CreateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        create_dto = CreateUserDto(**validator.data)
        user = await CreateUserInteractor().execute(dto=create_dto)
        return json({'data': user})


class BlockUser(HTTPMethodView):
    decorators = [is_jwt_authenticated]

    async def post(self, request: Request) -> Union[json, NoReturn]:
        token = TokenExtractor(request=request).extract()
        validator = BlockUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        block_dto = BlockUserDto(token, **validator.data)
        BlockUserInteractor().execute(dto=block_dto)
        return json({'data': True})


class DeactivateUser(HTTPMethodView):
    async def post(self, request: Request) -> Union[json, NoReturn]:
        pass


class UpdateUserToAdmin(HTTPMethodView):
    async def post(self, request: Request) -> Union[json, NoReturn]:
        pass
