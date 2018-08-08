from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    kayttajatunnus = StringField("käyttäjätunnus")
    salasana = PasswordField("salasana")
  
    class Meta:
        csrf = False