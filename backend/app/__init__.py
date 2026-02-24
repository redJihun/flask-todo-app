# app factory, Blueprint 등록
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .api import api_bp
from .config import DevelopmentConfig

db = SQLAlchemy()
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    CORS(app)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
