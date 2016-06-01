from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .firm import firm as firm_blueprint
    from .formation import formation as formation_blueprint
    from .user import user as user_blueprint
    from .contrat import contrat as contrat_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(firm_blueprint, url_prefix='/firm')
    app.register_blueprint(formation_blueprint, url_prefix='/formation')
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(contrat_blueprint, url_prefix='/contrat')

    return app
