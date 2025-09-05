from flask_login import UserMixin
from extensions import db 



# creating the user class 
class User(db.Model, UserMixin):

    __tablename__ = "users"

    #id (int),  user (txt), password (txt)

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email= db.Column(db.String(50),nullable = False, unique= True)
    cpf= db.Column(db.String(12),unique=True, nullable= False)






    


    





