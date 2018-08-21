from application import app, db
from flask import redirect, render_template, request, url_for
from application.questions.models import Question
from application.questions.forms import QuestionForm
from flask_login import login_required

@app.route("/questions", methods=["GET"])
@login_required
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
@login_required
def questions_form():
    return render_template("questions/new.html", form = QuestionForm())

@app.route("/questions/update/<question_id>", methods=["POST"])
@login_required
def questions_update(question_id):

    return render_template("questions/update.html", q = Question.query.get(question_id))


@app.route("/questions/delete/<question_id>", methods=["POST"])
@login_required
def questions_delete(question_id):
    q = Question.query.get(question_id)
    db.session().delete(q)
    db.session().commit()

    return redirect(url_for("questions_index"))      

@app.route("/questions/save/<question_id>", methods=["POST"])
@login_required
def question_save(question_id):
    q = Question.query.get(question_id)
    q.kysymys = request.form.get("nimi")
    q.kysymystyyppi = request.form.get("kysymystyyppi")
    db.session().commit()

    return redirect(url_for("questions_index"))

@app.route("/questions/", methods=["POST"])  
@login_required  
def questions_create():
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form = form)

    q = Question(form.kysymys.data, form.kysymystyyppi.data)

    db.session().add(q)
    db.session().commit()


    return redirect(url_for("questions_index"))