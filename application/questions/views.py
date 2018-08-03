from application import app, db
from flask import render_template, request
from application.questions.models import Question

@app.route("/questions/new/")
def questions_form():
    return render_template("questions/new.html")

@app.route("/questions/", methods=["POST"])    
def questions_create():
    q = Question(request.form.get("nimi"),request.form.get("kysymystyyppi"))

    db.session().add(q)
    db.session().commit()

    #print(request.form.get("nimi"))

    return "hello world!"