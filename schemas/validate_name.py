from flask import jsonify

def validate_name(name: str):
    if not name or len(name.strip()) < 3:
        return "Nome inválido. Deve conter pelo menos 3 caracteres.",400
    return None