from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class QuestionForm(FlaskForm):
    kysymys = StringField("kysymys", [validators.Length(min=1, max=500)])
    kysymystyyppi = SelectField("kysymystyyppi", choices=[("tiedekuntakohtainen", "tiedekuntakohtainen"), ("laitoskohtainen", "laitoskohtainen"),("kurssikohtainen", "kurssikohtainen")])

 
    class Meta:
        csrf = False