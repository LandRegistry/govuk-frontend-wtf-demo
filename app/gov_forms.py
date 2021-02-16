from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import GovCheckboxInput, GovPasswordInput, GovSubmitInput, GovTextInput
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, EqualTo, InputRequired, Length, Optional, Regexp


class GovBankDetailsForm(FlaskForm):
    name_on_the_account = StringField(
        "Name on the account",
        widget=GovTextInput(),
        validators=[InputRequired(message="Enter the name on the account")],
    )
    sort_code = StringField(
        "Sort code",
        widget=GovTextInput(),
        validators=[
            InputRequired(message="Enter a sort code"),
            Regexp(regex="\d{6}", message="Enter a valid sort code like 309430"),
        ],
        description="Must be 6 digits long",
    )
    account_number = StringField(
        "Account number",
        widget=GovTextInput(),
        validators=[
            InputRequired(message="Enter an account number"),
            Regexp(regex="\d{6,8}", message="Enter a valid account number like 00733445"),
            Length(min=6, max=8, message="Account number must be between 6 and 8 digits"),
        ],
        description="Must be between 6 and 8 digits long",
    )
    roll_number = StringField(
        "Building society roll number (if you have one)",
        widget=GovTextInput(),
        validators=[
            Optional(),
            Length(min=1, max=18, message="Building society roll number must be between 1 and 18 characters"),
            Regexp(
                regex="[a-zA-Z0-9- /.]*$",
                message="Building society roll number must only include letters a to z, numbers, hyphens, spaces, forward slashes and full stops",
            ),
        ],
        description="You can find it on your card, statement or passbook",
    )
    submit = SubmitField("Continue", widget=GovSubmitInput())


class GovCreateAccountForm(FlaskForm):
    first_name = StringField(
        "First name", widget=GovTextInput(), validators=[InputRequired(message="Enter your first name")]
    )
    last_name = StringField(
        "Last name", widget=GovTextInput(), validators=[InputRequired(message="Enter your last name")]
    )
    national_insurance_number = StringField(
        "National Insurance number",
        widget=GovTextInput(),
        validators=[
            InputRequired(message="Enter a National Insurance number"),
            Length(max=13, message="National Insurance number must be 13 characters or fewer"),
            Regexp(
                regex="^[a-zA-Z]{2}\d{6}[aAbBcCdD]$",
                message="Enter a National Insurance number in the correct format",
            ),
        ],
        description="It’s on your National Insurance card, benefit letter, payslip or P60. For example, ‘QQ 12 34 56 C’.",
    )
    email_address = StringField(
        "Email address",
        widget=GovTextInput(),
        validators=[
            InputRequired(message="Enter an email address"),
            Length(max=256, message="Email address must be 256 characters or fewer"),
            Email(message="Enter an email address in the correct format, like name@example.com"),
        ],
        description="You'll need this email address to sign in to your account",
    )
    telephone_number = StringField(
        "UK telephone number",
        widget=GovTextInput(),
        validators=[
            InputRequired(message="Enter a UK telephone number"),
            Regexp(
                regex="[\d \+]",
                message="Enter a telephone number, like 01632 960 001, 07700 900 982 or +44 0808 157 0192",
            ),
        ],
    )
    password = PasswordField(
        "Create a password",
        widget=GovPasswordInput(),
        validators=[
            InputRequired(message="Enter a password"),
            Length(min=8, message="Password must be at least 8 characters"),
        ],
        description="Must be at least 8 characters",
    )
    confirm_password = PasswordField(
        "Confirm password",
        widget=GovPasswordInput(),
        validators=[
            InputRequired(message="Confirm your password"),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    terms_and_conditions = BooleanField(
        "I agree to the terms and conditions",
        widget=GovCheckboxInput(),
        validators=[InputRequired(message="Select to confirm you agree with the terms and conditions")],
    )
    submit = SubmitField("Create account", widget=GovSubmitInput())
