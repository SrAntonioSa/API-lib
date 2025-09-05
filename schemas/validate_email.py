from flask import jsonify
from models import User

def validate_email(email: str):
    if not email or "@" not in email:
        return "Email inválido",400

    if User.query.filter_by(email=email).first():
        return  "Email já cadastrado", 409

    return None
