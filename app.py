from flask import Flask
from extensions import db
from dotenv import load_dotenv
from flask_login import LoginManager
import os
from api.routes_users import bp as users_bp
from api.routes_books import bp as books_bp
from api.routes_loans import bp as loans_bp
from models.user import User


load_dotenv()


# ...existing code...
def create_app():
    app = Flask(__name__)

  # Exemplo de conexão PostgreSQL:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.getenv("SECRET_KEY")  # obrigatório para sessões


    db.init_app(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(loans_bp)


    # Inicializa LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "users.login"  # endpoint de login do blueprint

    # Callback para carregar usuário pelo id
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)