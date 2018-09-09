from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.answers.models import Answer
from application.answers.forms import QuestionnaireForm
from application.questions.models import Question

@app.route("/answers/", methods=["GET"])
@login_required(role="opettaja")
def answers_index():
    return render_template("answers/list.html", answers = Answer.query.all())

@app.route("/questionnaire/")
@login_required(role="oppilas")
def questionnaire_form():

    form = QuestionnaireForm()

    return render_template("answers/questionnaire.html", form = form, kysymykset = Question.query.all())

@app.route("/questionnaire/save", methods=["POST"])
@login_required(role="oppilas")
def questionnaire_save():
    form = QuestionnaireForm(request.form)

    kysymys_id = request.form.get("kysymys_id", type=int)
  
    if not form.validate():
        return render_template("answers/questionnaire.html", form = form, kysymykset = Question.query.all())
  
    a = Answer(form.vastaus.data)
    a.kysymys_id = kysymys_id
  
    db.session().add(a)
    db.session().commit()
  
    return render_template("answers/questionnaire.html", form = form, kysymykset = Question.query.all())


@app.route("/questionnaire/answers")
@login_required(role="opettaja")
def show_answers():
    return render_template("answers/list.html", answers = Answer.query.all())
