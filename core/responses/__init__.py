from sanic.response import json


def response(body, status=200, headers=None, content_type="application/json"):
    return json(body={'data': body}, status=status, headers=headers, content_type=content_type)
