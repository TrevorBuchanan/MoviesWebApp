from flask import Flask
from config import Config
from flask_moment import Moment
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER 
    app.template_folder = config_class.TEMPLATE_FOLDER

    bootstrap.init_app(app)
    moment.init_app(app)
    
    # blueprint registration
    from app.Controller.errors import bp_errors as errors
    app.register_blueprint(errors)
    from app.Controller.routes import bp_routes as routes
    app.register_blueprint(routes)

    if not app.debug and not app.testing:
        pass
        # ... no changes to logging setup

    return app
