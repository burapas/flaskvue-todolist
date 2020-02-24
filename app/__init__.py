from flask import Flask

from config import config
from playhouse.flask_utils import FlaskDB

db = FlaskDB()


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    
    db.init_app(app) 


    @app.before_first_request
    def _db_ensure_closed():
        pass


    @app.before_request
    def _db_connect():
        if not db.database.is_closed():
            db.database.close()
        db.database.connect()

    
    @app.teardown_request
    def _db_close(exc):
        if not db.database.is_closed():
            db.database.close()

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app

