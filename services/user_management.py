from flask import jsonify, request
from models.database import db
from models.user import User
from werkzeug.security import generate_password_hash



def create_user(username: str, password: str, email: str, cpf: str ):
    # Verifica duplicatas
    if User.query.filter((User.username == username) | (User.email == email) | (User.cpf == cpf)).first():
        raise ValueError("Usuário, email ou CPF já cadastrado")
    
    # Gera hash da senha
    hashed_password = generate_password_hash(password)
    
    user = User(
        username=username,
        password=hashed_password,
        email=email,
        cpf=cpf
    )
    db.session.add(user)
    db.session.commit()
    return user


def login():
    return

def update():
    return

def delete():
    return





