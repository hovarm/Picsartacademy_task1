from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# engine = create_engine('sqlite:///C:/Users/Dell/Desktop/picsart_task1/clients.db')

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('user_id', db.Integer)
    name = db.Column(db.String(100), nullable = False)
    surname = db.Column(db.String(100), nullable = False)
    phone_num = db.Column(db.String(50), unique= True, nullable= False, primary_key=True)
    address = db.Column(db.String(200))

    def __init__(self, name, surname, phone_num, address):
        self.name = name
        self.surname = surname
        self.phone_num = phone_num
        self.address = address

    def __repr__(self):
        return f'<User: {self.name},{self.surname}, {self.phone_num}, {self.address} >'
db.create_all()




