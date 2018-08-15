from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(kayttajatunnus=form.kayttajatunnus.data, salasana=form.salasana.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Väärä käyttäjätunnus tai salasana")

    login_user(user)
    return redirect(url_for("index"))  

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))



@app.route("/auth/registration/")
@login_required
def registration_form():
    return render_template("auth/registration.html", form = RegistrationForm())


@app.route("/auth/", methods=["POST"])  
@login_required  
def users_create():
    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registration.html", form = form)

    u = User(form.nimi.data, form.kayttajatunnus.data, form.salasana.data, form.kayttajatyyppi.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))