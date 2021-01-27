from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class BankDetailsForm(FlaskForm):
    name_on_the_account = StringField("Name on the account")
    sort_code = StringField("Sort code", description="Must be 6 digits long")
    account_number = StringField("Account number", description="Must be between 6 and 8 digits long")
    roll_number = StringField(
        "Building society roll number (if you have one)",
        description="You can find it on your card, statement or passbook",
    )
    submit = SubmitField("Continue")
