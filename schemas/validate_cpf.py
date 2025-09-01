from flask import jsonify
from models import User
from validate_docbr import CPF

cpf_validator = CPF()

def validate_cpf(cpf: str):
    if not cpf_validator.validate(cpf):
        return jsonify({
            "message": "CPF inválido",
            "statusCode": 400
        }), 400

    if User.query.filter_by(cpf=cpf).first():
        return jsonify({
            "message": "CPF já cadastrado",
            "statusCode": 409
        }), 409

    return None
