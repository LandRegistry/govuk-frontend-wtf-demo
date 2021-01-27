import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "5L18nw&y6a^1HfYPzedcpSwq*82jYH9R"
