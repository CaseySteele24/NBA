from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import validators
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm): # inherit from FlaskForm
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # function to validate username and not allow repeats
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # if the user is none then it wont raise the following error
        if user:
            raise ValidationError('That username is taken. Please choose another one.')

    # function to validate email and not allow repeats
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        # if the email is none then it wont raise the following error
        if user:
            raise ValidationError('That email is taken. Please choose another one.')

class LoginForm(FlaskForm): # inherit from FlaskForm
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm): # inherit from FlaskForm
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # function to validate username and not allow repeats
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            # if the user is none then it wont raise the following error
            if user:
                raise ValidationError('That username is taken. Please choose another one.')

    # function to validate email and not allow repeats
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            # if the email is none then it wont raise the following error
            if user:
                raise ValidationError('That email is taken. Please choose another one.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')