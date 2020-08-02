from flask_login import UserMixin
from mainapp.__init__ import db,app



class ContactUs(db.Model,UserMixin):
    
    __tablename__='Contactus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10),  nullable=False)
    comments = db.Column(db.String(500), nullable=False)

class Donate(db.Model,UserMixin):
    
    __tablename__='Donation'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10),  nullable=False)
    food = db.Column(db.String(500), nullable=False)

class Partner(db.Model,UserMixin):
    
    __tablename__='Partner'

    id = db.Column(db.Integer, primary_key=True)
    orgname = db.Column(db.String(20), nullable=False)
    ownername = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(10),  nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    

