from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import GovTextInput
from wtforms import StringField
from wtforms.validators import InputRequired


class ExampleForm(FlaskForm):
    full_name = StringField(
        "Full name", widget=GovTextInput(), validators=[InputRequired(message="Enter your full name")]
    )
