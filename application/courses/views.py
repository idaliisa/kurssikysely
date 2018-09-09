from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.courses.models import Course
from application.auth.models import User, KurssiKayttaja
from application.courses.forms import CourseForm
from flask_login import current_user

@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
@login_required(role="paakayttaja")
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/update/<course_id>", methods=["POST"])
@login_required(role="paakayttaja")
def courses_update(course_id):

    return render_template("courses/update.html", c = Course.query.get(course_id))

@app.route("/courses/delete/<course_id>", methods=["POST"])
@login_required(role="paakayttaja")
def courses_delete(course_id):
    Course.poista_KurssiKayttaja(course_id)
    c = Course.query.get(course_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("courses_index"))      

@app.route("/courses/save/<course_id>", methods=["POST"])
@login_required(role="paakayttaja")
def course_save(course_id):
    c = Course.query.get(course_id)
    c.nimi = request.form.get("nimi")
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])  
@login_required (role="paakayttaja") 
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)

    c = Course(form.nimi.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/adduser/<course_id>", methods=["POST"])
@login_required(role="paakayttaja")
def add_users(course_id):
    return render_template("courses/adduser.html", course_id = course_id, users = User.query.all())
    
@app.route("/courses/<course_id>", methods=["POST"])
@login_required(role="paakayttaja")
def save_user(course_id):
    user_id = request.form.get("user_id")
    c = Course.query.get(course_id)
    u = User.query.get(user_id)
    c.kayttajat.append(u)
    db.session.add(c)
    db.session.commit()

    return redirect(url_for("courses_index"))