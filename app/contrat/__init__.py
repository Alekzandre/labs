from flask import Blueprint

contrat = Blueprint('contrat', __name__)

from . import views
