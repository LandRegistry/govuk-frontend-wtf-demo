from flask import flash, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFError

from app.demo import bp
from app.demo.forms import BankDetailsForm, CreateAccountForm, KitchenSinkForm


@bp.route("/forms/bank-details", methods=["GET", "POST"])
def bank_details():
    form = BankDetailsForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("main.index"))
    return render_template("bank_details.html", form=form)


@bp.route("/forms/create-account", methods=["GET", "POST"])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("main.index"))
    return render_template("create_account.html", form=form)


@bp.route("/forms/kitchen-sink", methods=["GET", "POST"])
def kitchen_sink():
    form = KitchenSinkForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("main.index"))
    return render_template("kitchen_sink.html", form=form)


@bp.errorhandler(CSRFError)
def csrf_error(error):
    flash("The form you were submitting has expired. Please try again.")
    return redirect(request.full_path)
