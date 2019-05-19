from sanic import Blueprint
from apps.users.views.v1 import User


bp = Blueprint('users', url_prefix='/api/v1')
bp.add_route(User.as_view(), '/users')
