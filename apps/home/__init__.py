from sanic import Blueprint
from apps.home.views import Home


bp = Blueprint('home')
bp.add_route(Home.as_view(), '/')
