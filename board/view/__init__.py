from flask import request, abort
from functools import wraps


def check_json(json):
    def decorator(func):
        @wraps(func)
        def wrapeer(*args, **kwargs):
            if not request.is_json:
                abort(400, "Check json format")

            for key, value in json.items():
                if key not in request.json or type(request.json[key]) is not value:
                    abort(400, "Check you json key name and value type")

            return func(*args, **kwargs)

        return wrapeer

    return decorator