from sanic import Blueprint
from apps.users.views.v1 import User, UserList


bp = Blueprint('users', url_prefix='/api/v1')
bp.add_route(UserList.as_view(), '/users')
bp.add_route(User.as_view(), '/users/<user_id:int>')
