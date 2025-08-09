from database import db 



class Book(db.Model):

    __tablename__ = "books"


    id = db.Column(db.Integer, primary_key= True)# book id
    title = db.Column(db.String(255),nullable= False)# book title
    author = db.Column(db.String(255),nullable = False)