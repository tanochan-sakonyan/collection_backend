from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)

    # Register Blueprints
    from .users import users_bp
    app.register_blueprint(users_bp)

    db.init_app(app)  # db をアプリに登録

    migrate = Migrate(app, db)  # migrate をアプリに登録
    

    return app