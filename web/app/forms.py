from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

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