from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
line_bot_api = None

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)

    global line_bot_api
    line_bot_api = app.config['LINE_CHANNEL_ACCESS_TOKEN']

    # モデルをインポートしてマッピングを登録
    from app.users import models as user_models
    from app.events import models as event_models
    from app.members import models as member_models

    # Register Blueprints
    from .users import users_bp
    app.register_blueprint(users_bp)
    from .events import events_bp
    app.register_blueprint(events_bp)
    from .members import members_bp
    app.register_blueprint(members_bp)

    db.init_app(app)  # db をアプリに登録

    migrate = Migrate(app, db)  # migrate をアプリに登録
    

    return app