from flask import Blueprint

bp = Blueprint("order", __name__, url_prefix="/orders")

from . import routes  # noqa F401
