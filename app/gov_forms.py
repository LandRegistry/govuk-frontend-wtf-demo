from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import GovSubmitInput, GovTextInput
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class ExampleForm(FlaskForm):
    full_name = StringField(
        "Full name", widget=GovTextInput(), validators=[InputRequired(message="Enter your full name")]
    )
    submit = SubmitField("Continue", widget=GovSubmitInput())
