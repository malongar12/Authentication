from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    firstName = StringField("first Name", validators=[InputRequired()])
    lastName = StringField("last Name", validators=[InputRequired()])
    userName = StringField("create a username", validators=[InputRequired()])
    email = EmailField("email", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
   
    
    
    
    
class LoginForm(FlaskForm):
    userName = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
    
    
class FeedbackForm(FlaskForm):
    """Add feedback form."""
    title = StringField("Title", validators=[InputRequired()])
    content = StringField( "Content", validators=[InputRequired()])
    