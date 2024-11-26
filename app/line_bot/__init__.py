from flask import Blueprint

line_bot_bp = Blueprint('line_bot', __name__)

from . import handlers