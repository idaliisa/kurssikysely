from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.answers.models import Answer
from application.answers.forms import QuestionnaireForm
from application.questions.models import Question

@app.route("/questionnaire", methods=["GET", "POST"])
@login_required
def questionnaire_form():
    form = QuestionnaireForm(request.form)
    
    if not form.validate():
        return render_template("answers/questionnaire.html",  kysymykset = Question.query.all(), form = form)

    
    return render_template("answers/questionnaire.html",  kysymykset = Question.query.all(), form = form)
