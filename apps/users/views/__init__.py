from sanic import Blueprint
from apps.users.views.v1 import User, UserList, BlockUser, DeactivateUser, Login


bp = Blueprint('users', url_prefix='/api/v1')
bp.add_route(UserList.as_view(), '/users')
bp.add_route(Login.as_view(), '/users/login')
bp.add_route(User.as_view(), '/users/<user_id:int>')
bp.add_route(BlockUser.as_view(), '/users/<user_id:int>/block')
bp.add_route(DeactivateUser.as_view(), '/users/<user_id:int>/deactivate')
