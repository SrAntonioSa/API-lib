from flask import jsonify
from models import User
from validate_docbr import CPF

cpf_validator = CPF()

def validate_cpf(cpf: str):
    if not cpf_validator.validate(cpf):
        return  "CPF inválido",400

    if User.query.filter_by(cpf=cpf).first():
        return "CPF já cadastrado", 409

    return None

