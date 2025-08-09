
from services.user_management import create_user
from flask import Flask, jsonify


app = Flask(__name__)



@app.route("/create_user", methods = ["POST"])
def create_user():

    #chama o schemas para validar os dados inseridos

    #chama a funçao de criar usuario services 

    return jsonify({"message":"usuario criado com sucesso"})


@app.route("/login", methods = ["POST"])
def login():

    # verifica os dados inseridos

    # verifica se o usuario inserido existe 
      
    return jsonify({"message":"login realizado com sucesso"})

      
@app.route("/logout", methods = ["GET"])
def logout():
        
    # verifica se o usuario esta conectado

    # desconectar o usuario

    return jsonify({"message":"usuario criado com sucesso"})


@app.route("/update", methods = ["PUT"])
def update_user():
     
    # verifica se o usuario esta logado

    # recebe os dados 

    # verifica os dados

    # pede a senha

    return jsonify({"message":"usuario atualizado com socesso"})


@app.route("/delete", methods = ["DELETE"])
def delete_user():

    # verifica se o usuario esta logado

    # confirma que os dados serao eliminados definitivamente

    # pede a senha

    # elimona o usuario

    return jsonify({"message":"usuario eliminado"})






