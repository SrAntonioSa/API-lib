from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/register_book", methods = ["POST"])
def new_book():

    # verifica se os dados inseridos estao corretos, chamando o esquema para verificar livros

    # chama a funçao que registra novos livros

    return jsonify({"message":"new book added to the catalog"})



@app.route("/register_delete_book", methods = ["DELETE"])
def remove_book():

    # verifica o id do livro

    # chama a funcao que remove o livro 

    return jsonify({"message":"Book removed from the catalog"})



    
