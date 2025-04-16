from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from app import Product, Buyer, store


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    role = RadioField('Role', choices=[('buyer', 'Покупатель'), ('saler', 'Продавец')], validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    role = RadioField('Role', choices=[('buyer', 'Покупатель'), ('saler', 'Продавец')], validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data, role=self.role.data).first()
        if user is not None:
            raise ValidationError('Имя уже занято для этой роли.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data, role=self.role.data).first()
        if user is not None:
            raise ValidationError('Email уже зарегистрирован для этой роли.')
        
class SalerAddProductForm(FlaskForm):
    name = StringField('Name of product',validators=[DataRequired()])
    price = FloatField('Price of product',validators=[DataRequired()])
    count = IntegerField('Count of product',validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_price(self,price):
        try:
            Product("a",float(price.data),1)
        except Exception as er:
            raise ValidationError("Цена должна быть числом больше нуля.")
    
    def validate_count(self,count):
        try:
            Product("a",1,int(count.data))
        except Exception as er:
            raise ValidationError("Количество товара должно быть целочисленным числом больше нуля.")
    
class BuyerAddMoneyForm(FlaskForm):
    money = FloatField('Sum',validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_money(self,money):
        try:
            b = Buyer("byr","b00")
            b.money += money.data
        except Exception as er:
            raise ValidationError("Сумма должна быть числом больше 0")

class BuyProductForm(FlaskForm):
    salername = StringField("Saler name",validators=[DataRequired()])
    productname = StringField("Product name",validators=[DataRequired()])
    count = IntegerField("Count of product",validators=[DataRequired()])
    submit = SubmitField('Buy')


    def validate_salername(self,salername):
        if salername.data not in store.salers:
            raise ValidationError("Такого продовца нет.")
    
    def validate_productname(self,productname):
        if self.salername.data in store.salers and productname.data not in store.salers[self.salername.data].products:
            raise ValidationError(f"У продавца {self.salername.data} нет такого товара.")
        
    def validate_count(self,count):
        if count.data > store.salers[self.salername.data].products[self.productname.data].count:
            raise ValidationError("У продавца нет столько товара")
        
            