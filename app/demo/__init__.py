from flask import Blueprint

bp = Blueprint("demo", __name__, template_folder="../templates/demo")

from app.demo import routes  # noqa: E402,F401
