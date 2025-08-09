
from database import db 



# creating the user class 
class User(db.Model,):

    __tablename__ = "Users"

    #id (int),  user (txt), password (txt)

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(50),nullable = False, unique= True)
    cpf= db.Column(db.String(12),unique=True, nullable= False)

    # creating a relationship between class user and class loan 
    # relationship 1:N
    # loans is a list of loans from this user





    # relationship between book and loan
    




    


    





