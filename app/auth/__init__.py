#app/auth/__init.py__
from flask import Blueprint
authentication = Blueprint('authentication', __name__, template_folder='templates')
from app.auth import routes
