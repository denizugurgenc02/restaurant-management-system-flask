from flask import Blueprint

bp = Blueprint("table", __name__, url_prefix="/tables")

from . import routes  # noqa F401
