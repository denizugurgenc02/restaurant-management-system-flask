from flask import Blueprint

bp = Blueprint("product", __name__, url_prefix="/products")

from . import routes  # noqa F401
