from flask import Flask
from models.database import db

from api.routes_users import bp as users_bp
from api.routes_books import bp as books_bp
from api.routes_loans import bp as loans_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(loans_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)