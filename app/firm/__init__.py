from flask import Blueprint

firm = Blueprint('firm', __name__)

from . import views
