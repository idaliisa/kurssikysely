from application import app, db
from flask import redirect, render_template, request, url_for
from application.questions.models import Question
from flask_login import login_required

@app.route("/questions", methods=["GET"])
@login_required
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
@login_required
def questions_form():
    return render_template("questions/new.html")

@app.route("/questions/update/", methods=["POST"])
@login_required
def questions_update():
    id = request.form.get("question_id", type=int)
    return render_template("questions/update.html", q = Question.query.get(id))

####
@app.route("/questions/delete/", methods=["POST"])
@login_required
def questions_delete():
    id = request.form.get("question_id", type=int)
    q = Question.query.get(id)
    db.session().delete(q)
    db.session().commit()

    return redirect(url_for("questions_index"))      

@app.route("/questions/save/", methods=["POST"])
@login_required
def question_save():
    id = request.form.get("question_id", type=int)
    q = Question.query.get(id)
    q.kysymys = request.form.get("nimi")
    q.kysymystyyppi = request.form.get("kysymystyyppi")
    db.session().commit()

    return redirect(url_for("questions_index"))

@app.route("/questions/", methods=["POST"])  
@login_required  
def questions_create():
    q = Question(request.form.get("nimi"),request.form.get("kysymystyyppi"))

    db.session().add(q)
    db.session().commit()


    return redirect(url_for("questions_index"))