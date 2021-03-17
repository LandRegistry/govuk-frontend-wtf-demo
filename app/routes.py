import json

from flask import flash, make_response, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFError

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
    # Default cookies policy to reject all categories of cookie
    cookies_policy = {"functional": "no", "analytics": "no"}

    # Create the response up front so we can set the cookie before returning
    response = make_response(render_template("cookies.html", title="Cookies", form=form))

    if form.validate_on_submit():
        print("Form validated on submit")
        # Update cookies policy consent from form data
        print("Setting functional cookie consent to {}".format(form.functional.data))
        cookies_policy["functional"] = form.functional.data
        print("Setting analytics cookie consent to {}".format(form.analytics.data))
        cookies_policy["analytics"] = form.analytics.data

        # Set cookies policy for one year
        print("Setting cookies_policy cookie to {}".format(json.dumps(cookies_policy)))
        response.set_cookie("cookies_policy", json.dumps(cookies_policy), max_age=31557600)

        # Confirm to the user and return response
        flash("You’ve set your cookie preferences.", "success")
        return response
    elif request.method == "GET":
        if request.cookies.get("cookies_policy"):
            # Set cookie consent radios data to current policy
            print("Found existing cookie policy {}".format(request.cookies.get("cookies_policy")))
            cookies_policy = json.loads(request.cookies.get("cookies_policy"))
            print("Setting functional cookie consent radio to existing {}".format(cookies_policy["functional"]))
            form.functional.data = cookies_policy["functional"]
            print("Setting analytics cookie consent radio to existing {}".format(cookies_policy["analytics"]))
            form.analytics.data = cookies_policy["analytics"]
        else:
            # If conset not previously set, use default "no" policy
            print("No existing cookie policy found, using default policy {}".format(cookies_policy))
            print("Setting functional cookie consent radio to default {}".format(cookies_policy["functional"]))
            form.functional.data = cookies_policy["functional"]
            print("Setting analytics cookie consent radio to default {}".format(cookies_policy["analytics"]))
            form.analytics.data = cookies_policy["analytics"]
    return response


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
