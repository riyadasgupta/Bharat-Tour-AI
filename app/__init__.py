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