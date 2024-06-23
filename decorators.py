from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
from models import User

def check_access(role):
    def wrapper(func):
        @wraps(func)
        @jwt_required()
        def decorator(*args, **kwargs):
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            if user and user.get_role() == role:
                return func(*args, **kwargs)
            else:
                return jsonify({"message": "Unauthorized access"}), 403
        return decorator
    return wrapper
