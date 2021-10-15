import json

from flask import flash, make_response, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFError

from app import app
from app.forms import BankDetailsForm, CookiesForm, CreateAccountForm, KitchenSinkForm


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


@app.route("/forms/kitchen-sink", methods=["GET", "POST"])
def kitchen_sink():
    form = KitchenSinkForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("index"))
    return render_template("kitchen_sink.html", form=form)


@app.route("/cookies", methods=["GET", "POST"])
def cookies_page():
    form = CookiesForm()
    # Default cookies policy to reject all categories of cookie
    cookies_policy = {"functional": "no", "analytics": "no"}

    if form.validate_on_submit():
        # Update cookies policy consent from form data
        cookies_policy["functional"] = form.functional.data
        cookies_policy["analytics"] = form.analytics.data

        # Create flash message confirmation before rendering template
        flash(
            "<p class='govuk-notification-banner__heading'>You’ve set your cookie preferences. <a class='govuk-notification-banner__link' href='{}'>Go back to the page you were looking at</a>.</p>".format(
                url_for("index")
            ),
            "success",
        )

        # Create the response so we can set the cookie before returning
        response = make_response(render_template("cookies.html", form=form))

        # If cookies have been declined, remove any existing ones from previous acceptances
        if form.functional.data == "no":
            response.delete_cookie("your_functional_cookie")
        elif form.analytics.data == "no":
            response.delete_cookie("your_analytics_cookie")

        # Set cookies policy for one year
        response.set_cookie(
            "cookies_policy",
            json.dumps(cookies_policy),
            max_age=31557600,
            samesite="Lax",
        )
        return response
    elif request.method == "GET":
        if request.cookies.get("cookies_policy"):
            # Set cookie consent radios to current consent
            cookies_policy = json.loads(request.cookies.get("cookies_policy"))
            form.functional.data = cookies_policy["functional"]
            form.analytics.data = cookies_policy["analytics"]
        else:
            # If conset not previously set, use default "no" policy
            form.functional.data = cookies_policy["functional"]
            form.analytics.data = cookies_policy["analytics"]
    return render_template("cookies.html", form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server(error):
    return render_template("500.html"), 500


@app.errorhandler(CSRFError)
def csrf_error(error):
    flash("The form you were submitting has expired. Please try again.")
    return redirect(request.full_path)
