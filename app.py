from flask import Flask
from extensions import db
from dotenv import load_dotenv
import os
from api.routes_users import bp as users_bp
from api.routes_books import bp as books_bp
from api.routes_loans import bp as loans_bp


load_dotenv()


# ...existing code...
def create_app():
    app = Flask(__name__)

  # Exemplo de conexão PostgreSQL:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(loans_bp)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)