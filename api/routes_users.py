from flask import  jsonify, Blueprint
from services.user_management import create_user, login
from flask_login import login_required



bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/create_user", methods = ["POST"])
def create():

    create_user()

    return jsonify({"message":"usuario criado com sucesso"})


@bp.route("/login", methods = ["POST"])
@login_required
def login():

    login()

      
    return jsonify({"message":"login realizado com sucesso"})

      
@bp.route("/logout", methods = ["GET"])
def logout():
        
    # verifica se o usuario esta conectado

    # desconectar o usuario

    return jsonify({"message":"usuario criado com sucesso"})


@bp.route("/update", methods = ["PUT"])
def update_user():
     
    # verifica se o usuario esta logado

    # recebe os dados 

    # verifica os dados

    # pede a senha

    return jsonify({"message":"usuario atualizado com socesso"})


@bp.route("/delete", methods = ["DELETE"])
@login_required
def delete_user():
    




    return jsonify({"message":"usuario eliminado"})






