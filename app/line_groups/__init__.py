from flask import Blueprint

line_groups_bp = Blueprint('lien_groups', __name__)

from . import routes