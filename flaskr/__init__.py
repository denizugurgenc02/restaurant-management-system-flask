import importlib
import pkgutil

from flask import Blueprint, Flask

from flaskr.core.config import config_by_name
from flaskr.core.extensions import db, migrate

DEFAULT_CONFIG = "development"


def load_all_models():  # Necessary for migrate command
    domain_package = importlib.import_module(".domains", __name__)
    package_dir = domain_package.__path__[0]

    for _, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
        if is_pkg:
            model_module_path = f".domains.{module_name}.models"
            try:
                importlib.import_module(model_module_path, __name__)
                print(f"Loaded model: {model_module_path}")
            except ImportError as e:
                if "No module named" not in str(e):
                    raise e


def register_blueprints(app: Flask):  # Registration to endpoints. --SOLID--
    domain_package = importlib.import_module(".domains", __name__)
    package_dir = domain_package.__path__[0]

    for _, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
        if is_pkg:
            module_path = f".domains.{module_name}"
            module = importlib.import_module(module_path, __name__)

            if hasattr(module, "bp") and isinstance(module.bp, Blueprint):
                blueprint = module.bp
                app.register_blueprint(blueprint)
                print(f"Successfully registered blueprint: {blueprint.name}")


def create_app(config_name: str = DEFAULT_CONFIG):
    config_class = config_by_name.get(config_name)
    if config_class is None:
        raise ValueError(f"Invalid configuration name: {config_name}")

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        load_all_models()

    register_blueprints(app)

    return app
