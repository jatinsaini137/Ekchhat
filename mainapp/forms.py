from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,  ValidationError
from mainapp.models import ContactUs
from mainapp.__init__ import db
from flask_sqlalchemy import SQLAlchemy


class ContactUsForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    address = StringField('address', validators=[DataRequired(), Length(min=5, max=100)])
    phone = StringField('phone', validators=[DataRequired(), Length(min=10, max=10)])
    comments = StringField('comments', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit')


    
    def validate_email(self,email):
        
        email = ContactUs.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email I.D already registered')

class DonateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    address = StringField('address', validators=[DataRequired(), Length(min=5, max=100)])
    phone = StringField('phone', validators=[DataRequired(), Length(min=10, max=10)])
    food = StringField('food', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit')


class PartnerForm(FlaskForm):
    orgname = StringField('orgname', validators=[DataRequired(), Length(min=2, max=20)])
    ownername = StringField('ownername', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    phone = StringField('phone', validators=[DataRequired(), Length(min=10, max=10)])
    state = StringField('state', validators=[DataRequired(), Length(min=5, max=100)])
    city = StringField('city', validators=[DataRequired(), Length(min=5, max=100)])
    address = StringField('address', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Submit')


db.create_all()



    
        
