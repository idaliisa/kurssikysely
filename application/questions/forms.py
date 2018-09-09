from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class QuestionForm(FlaskForm):
    kysymys = StringField("kysymys", [validators.Length(min=1, max=500)])
 
    class Meta:
        csrf = False