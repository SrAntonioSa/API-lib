from flask import jsonify

def validate_password(password: str):
    if not password or len(password) < 8:
        return "Senha inválida. Deve ter pelo menos 8 caracteres.",400
    return None
