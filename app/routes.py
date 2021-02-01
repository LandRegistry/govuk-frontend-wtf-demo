from flask import redirect, render_template, url_for

from app import app
from app.forms import BankDetailsForm, CreateAccountForm


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/forms/bank-details", methods=["GET", "POST"])
def bank_details():
    form = BankDetailsForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("bank_details.html", form=form)


@app.route("/forms/create-account", methods=["GET", "POST"])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("create_account.html", form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server(error):
    return render_template("500.html"), 500
