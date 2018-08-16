from flask_wtf import FlaskForm
from wtforms import StringField, validators

class QuestionnaireForm(FlaskForm):
    vastaus = StringField("vastaus", [validators.Length(min=1, max=500)])
    
    class Meta:
        csrf = False