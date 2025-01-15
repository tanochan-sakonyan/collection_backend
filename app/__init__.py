from flask import Flask
from google.cloud import firestore
from app.config import Config
from flask_migrate import Migrate
from linebot import LineBotApi, WebhookHandler

db = firestore.Client()
line_bot_api = None
handler = None

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)

    global line_bot_api
    if app.config['LINE_CHANNEL_ACCESS_TOKEN']:
        line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])  # global handler
    global handler
    if app.config['LINE_CHANNEL_SECRET']:
        handler = WebhookHandler(app.config['LINE_CHANNEL_SECRET'])  # global handler
    


    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    return app