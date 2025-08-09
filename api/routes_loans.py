from flask import Flask, jsonify, Blueprint



app = Flask(__name__)

bp = Blueprint("loans", __name__, url_prefix="/loans")


@app.route("/register_loan_book", methods = ["POST"])
def new_loan():

    # verifica o id do livro

    # verifica o id do usuario

    # chama a funçao que cria novos emprestimos

    return jsonify({"message":"new book added to the catalog"})


@app.route("/register_return_book", methods = ["PUT"])
def return_book():

    # verifica o id do emprestimo

    # chama a funçao que registra a devoluçao

   

    return jsonify({"message":"Book returned"})
  