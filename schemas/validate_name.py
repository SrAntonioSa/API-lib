from flask import jsonify

def validate_name(name: str):
    if not name or len(name.strip()) < 3:
        return jsonify({
            "message": "Nome inválido. Deve conter pelo menos 3 caracteres.",
            "statusCode": 400
        }), 400
    return None