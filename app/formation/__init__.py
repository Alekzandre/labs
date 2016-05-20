from flask import Blueprint

formation = Blueprint('formation', __name__)

from . import views
