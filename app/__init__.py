# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap
# from flask_login import LoginManager
# from config import Config

# db = SQLAlchemy()
# bootstrap = Bootstrap()
# login_manager = LoginManager()
# login_manager.login_view = 'main.login'  # Changed from 'auth.login' to 'main.login'

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     db.init_app(app)
#     bootstrap.init_app(app)
#     login_manager.init_app(app)

#     from app.routes import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     # Removed the auth blueprint registration since we're handling auth in routes.py

#     with app.app_context():
#         db.create_all()
#         # Load initial data if needed
#         from app.recommender import load_initial_data
#         load_initial_data()

#     return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    with app.app_context():
        db.create_all()
    
    return app

from app import models