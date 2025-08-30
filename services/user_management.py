from flask import jsonify, request
from extensions import db
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
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

        data = request.json
        username= data.get("username")
        password = data.get("password")

        if username and password:
        #login
            if username and password:

            
                user = User.query.filter_by(username=username).first() # buscando o usuario no bando de dados 

                # verificando o usuario e a senha encriptada pelo bcrypt, sempre usando o str.encode para transformar a string em bytes 
                if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
                    login_user(user) #inicia sessao com o usuario
                    print(current_user.is_authenticated) # mostra o usuario atual como logado : is_autenticated = true
                    return jsonify({"message": "Autenticaçao realizada com sucesso "})


        return jsonify({"message": "credenciais invalidas"}), 400
    

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
       
    if  id == current_user.id:
        return jsonify({"message": " deleçao nao permitida"}),403
    
    # quelquer usuario pode apagar deletar, ate que seja implementada a funçao de admin, restringindo essa funçao 
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuario{id} deletado com sucesso"})
    
        
    return jsonify({"message": " Usuario nao encontrado"}),404
    





