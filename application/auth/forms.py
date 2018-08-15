from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):
    kayttajatunnus = StringField("käyttäjätunnus", [validators.Length(min=5, max=50)])
    salasana = PasswordField("salasana", [validators.Length(min=5, max=50)])
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    nimi = StringField("nimi", [validators.Length(min=5, max=50)])
    kayttajatunnus = StringField("käyttäjätunnus", [validators.Length(min=5, max=50)])
    salasana = PasswordField("salasana", [validators.Length(min=5, max=50)])
    kayttajatyyppi = SelectField("käyttäjätyyppi", choices=[("paakayttaja", "pääkäyttäjä"), ("laitoshlo", "laitoksen vastuuhenkilö"),("opettaja", "opettaja"),("oppilas", "oppilas")])

    class Meta:
        csrf = False