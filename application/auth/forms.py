from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):
    kayttajatunnus = StringField("käyttäjätunnus", [validators.Length(min=5)])
    salasana = PasswordField("salasana", [validators.Length(min=5)])
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    nimi = StringField("nimi", [validators.Length(min=5)])
    kayttajatunnus = StringField("käyttäjätunnus", [validators.Length(min=5)])
    salasana = PasswordField("salasana", [validators.Length(min=5)])
    kayttajatyyppi = SelectField("käyttäjätyyppi", choices=[("text", "pääkäyttäjä"), ("text", "laitoksen vastuuhenkilö"),("text", "opettaja"),("text", "oppilas")])

    class Meta:
        csrf = False