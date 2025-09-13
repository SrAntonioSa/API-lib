from flask import jsonify, request
import bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user

from extensions import db
from models.user import User
from schemas.validate_name import validate_name
from schemas.validate_email import validate_email
from schemas.validate_cpf import validate_cpf
from schemas.validate_password import validate_password



def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    cpf = data.get("cpf")


    for validator, value in [
        (validate_name, username),
        (validate_email, email),
        (validate_cpf, cpf),
        (validate_password, password)
    ]:
        error = validator(value)
        if error:
            return jsonify({"error": error}), 400



    if username and password:  
        hashed_password= bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        hashed_password = hashed_password.decode("utf-8")
        user = User(username = username, password = hashed_password  , email = email, cpf = cpf )
        db.session.add(user) 
        db.session.commit()
        return jsonify({
                    "name":f"{username}",
                    "email":f"{email}",
                    "cpf":f"{cpf}"
          })

    return jsonify({"message": " dados invalidos"}), 400

def login():
    
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    # busca usuário pelo email
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Email ou senha incorretos"}), 401

    # verifica senha
    if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return jsonify({"error": "Email ou senha incorretos"}), 401

    # loga o usuário no Flask-Login
    login_user(user)

    return jsonify({
            "user": {
                "username": user.username,
                "uuid": str(user.uuid)  # garante que sai como string
            }
        }), 200




def update_password():
        
    data = request.json # lendo os dados 
    user = User.query.get(id) # procurando a id do usuario

    if id != current_user.id:# verificando se a id e a do usuario atual 
        return jsonify({"message": "Operaçao nao permitida"}), 403

    if user and data.get("password") :
        user.password = data.get("password")
        db.session.commit()

        return jsonify({"message": f" usuario {id} atualizado com sucesso"})
    
    
    
    return jsonify({"message": " Usuario nao encontrado"}),404
    

def delete():

    user = User.query.get(id)
       
    if id == current_user.id:
        return jsonify({"message": " deleçao nao permitida"}),403
    # quelquer usuario pode apagar deletar, ate que seja implementada a funçao de admin, restringindo essa funçao 
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuario{id} deletado com sucesso"})       
    return jsonify({"message": " Usuario nao encontrado"}),404
