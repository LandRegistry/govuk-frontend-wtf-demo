from flask import flash, redirect, render_template, request, url_for

from app import app
from app.forms import BankDetailsForm, CookiesForm, CreateAccountForm


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/forms/bank-details", methods=["GET", "POST"])
def bank_details():
    form = BankDetailsForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("index"))
    return render_template("bank_details.html", form=form)


@app.route("/forms/create-account", methods=["GET", "POST"])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("index"))
    return render_template("create_account.html", form=form)


@app.route("/cookies", methods=["GET", "POST"])
def cookies_page():
    form = CookiesForm()
    if form.validate_on_submit():
        flash("<p class='govuk-notification-banner__heading'>You’ve set your cookie preferences. <a href={} class='govuk-notification-banner__link'>Go back to the page you were looking at</a>.</p>".format(url_for("index")), "success")
    return render_template("cookies.html", form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server(error):
    return render_template("500.html"), 500
