from flask import Blueprint

bp = Blueprint("user", __name__, url_prefix="/users")

from . import routes  # noqa F401
