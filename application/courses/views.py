from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.courses.models import Course
from application.auth.models import User
from application.courses.forms import CourseForm
from flask_login import current_user, login_required

@app.route("/courses", methods=["GET"])
@login_required
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/update/<course_id>", methods=["POST"])
@login_required
def courses_update(course_id):

    return render_template("courses/update.html", c = Course.query.get(course_id))


@app.route("/courses/delete/<course_id>", methods=["POST"])
@login_required
def courses_delete(course_id):
    c = Course.query.get(course_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("courses_index"))      

@app.route("/courses/save/<course_id>", methods=["POST"])
@login_required
def course_save(course_id):
    c = Course.query.get(course_id)
    c.nimi = request.form.get("nimi")
    c.laitos = request.form.get("laitos")
    c.tiedekunta = request.form.get("tiedekunta")
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])  
@login_required  
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)

    c = Course(form.nimi.data, form.laitos.data, form.tiedekunta.data)

    db.session().add(c)
    db.session().commit()


    return redirect(url_for("courses_index"))

