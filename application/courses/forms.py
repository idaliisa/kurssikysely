from flask_wtf import FlaskForm
from wtforms import StringField, validators
  
class CourseForm(FlaskForm):
    nimi = StringField("nimi", [validators.Length(min=5, max=50)])
    laitos = StringField("laitos", [validators.Length(min=5, max=50)])
    tiedekunta = StringField("tiedekunta", [validators.Length(min=5, max=50)])
  
    class Meta:
        csrf = False