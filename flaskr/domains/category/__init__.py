from flask import Blueprint

bp = Blueprint("category", __name__, url_prefix="/categories")

from . import routes  # noqa F401
