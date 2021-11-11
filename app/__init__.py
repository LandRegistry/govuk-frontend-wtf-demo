from flask import Flask
from flask_assets import Bundle, Environment
from flask_compress import Compress
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from govuk_frontend_wtf.main import WTFormsHelpers
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

from config import Config

csrf = CSRFProtect()
compress = Compress()
talisman = Talisman()
assets = Environment()


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="/assets")
    app.config.from_object(config_class)
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True
    app.jinja_loader = ChoiceLoader(
        [
            PackageLoader("app"),
            PrefixLoader(
                {
                    "govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja"),
                    "govuk_frontend_wtf": PackageLoader("govuk_frontend_wtf"),
                }
            ),
        ]
    )

    assets.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)
    csp = {
        "default-src": "'self'",
        "script-src": [
            "'self'",
            "'sha256-+6WnXIl4mbFTCARd8N3COQmT3bJJmo32N8q8ZSQAIcU='",
            "'sha256-l1eTVSK8DTnK8+yloud7wZUqFrI0atVo6VlC6PJvYaQ='",
        ],
        "img-src": ["data:", "'self'"],
    }
    talisman.init_app(app, content_security_policy=csp)

    js = Bundle("src/js/*.js", filters="jsmin", output="dist/js/custom-%(version)s.js")
    if "js" not in assets:
        assets.register("js", js)

    WTFormsHelpers(app)

    # Register blueprints
    from app.main import bp as main_bp
    from app.demo import bp as demo_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(demo_bp)

    return app
