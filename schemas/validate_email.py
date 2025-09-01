from flask import jsonify
from models import User

def validate_email(email: str):
    if not email or "@" not in email:
        return jsonify({
            "message": "Email inválido",
            "statusCode": 400
        }), 400

    if User.query.filter_by(email=email).first():
        return jsonify({
            "message": "Email já cadastrado",
            "statusCode": 409
        }), 409

    return None
