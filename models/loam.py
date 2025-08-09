from datetime import datetime
from models.database import db


class Loan(db.Model):
    
    __tablename__ = "loans"  # Nome da tabela intermediária

    id = db.Column(db.Integer, primary_key=True)  # Chave primária do empréstimo
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # FK para usuário
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)  # FK para livro
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)  # Data do empréstimo, padrão agora
    return_date = db.Column(db.DateTime, nullable=True)  # Data da devolução, pode ser nula (não devolvido ainda)
    returned = db.Column(db.Boolean, default=False) 