from flask import jsonify, request
from extensions import db
from models.user import User
import bcrypt


def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    cpf = data.get("cpf")
    if username and password:  
        hashed_password= bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username = username, password = hashed_password  , email = email, cpf = cpf )
        db.session.add(user)
        db.session.commit()  
    return 


def login():
    return

def update():
    return

def delete():
    return





