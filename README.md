# API-lib
an api that has users, authentication database and encrypted passwords



The "api" folder contaisn the routes for  users, books and loans

The "models" folder contains the classes of the objects that will be used in the project

The "schemas" folder contains the pydantic verification rules

The "services" folder contains the business rules that will be called when a given route is accessed

firt of all to run the app you need to setup your database preferences, the app, user, password and database_name 


to run the app:
on  terminal
1 pip install -r requirements.txt
2 python
 from extensions import db
 from models import User, Book, Loan
 exit()
3 flask shell
 db.drop_all()
 db.create_all()
 db.session.commit()
 exit()

run app.py and you can test on postman and your SQL client 

postgresql+psycopg2://username:password@localhost:5432/postgdatabase_nnameres