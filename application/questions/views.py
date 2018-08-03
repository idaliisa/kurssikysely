from application import app, db
from flask import redirect, render_template, request, url_for
from application.questions.models import Question

@app.route("/questions", methods=["GET"])
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
def questions_form():
    return render_template("questions/new.html")

@app.route("/questions/update/", methods=["POST"])
def questions_update():
    id = request.form.get("question_id", type=int)
    return render_template("questions/update.html", q = Question.query.get(id))

@app.route("/questions/save/", methods=["POST"])
def question_save():
    #q = Question(request.form.get("id"), request.form.get("nimi"),request.form.get("kysymystyyppi"))
    id = request.form.get("question_id", type=int)
    q = Question.query.get(id)
    q.kysymys = request.form.get("nimi")
    q.kysymystyyppi = request.form.get("kysymystyyppi")
    db.session().commit()

    return redirect(url_for("questions_index"))

@app.route("/questions/", methods=["POST"])    
def questions_create():
    q = Question(request.form.get("nimi"),request.form.get("kysymystyyppi"))

    db.session().add(q)
    db.session().commit()


    return redirect(url_for("questions_index"))