from flask import Blueprint

members_bp = Blueprint('menbers', __name__)

from . import routes