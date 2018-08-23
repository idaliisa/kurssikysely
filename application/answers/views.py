from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.answers.models import Answer
from application.answers.forms import QuestionnaireForm
from application.questions.models import Question

@app.route("/answers/", methods=["GET"])
def answers_index():
    return render_template("answers/list.html", answers = Answer.query.all())

@app.route("/questionnaire/")
#@login_required
def questionnaire_form():

    form = QuestionnaireForm()

    return render_template("answers/questionnaire.html", form = form, kysymykset = Question.query.all())

@app.route("/questionnaire/save", methods=["POST"])
#@login_required
def questionnaire_save():
    form = QuestionnaireForm(request.form)

    kysymys_id = request.form.get("kysymys_id", type=int)
  
    if not form.validate():
        return render_template("questionnaire.html", form = form, kysymykset = Question.query.all())
  
    a = Answer(form.vastaus.data)
    a.kysymys_id = kysymys_id
  
    db.session().add(a)
    db.session().commit()
  
    return redirect(url_for("answers_index"))