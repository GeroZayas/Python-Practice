#Run pip install flask-blueprint
from flask import Blueprint



views = Blueprint('views')

@views.route('/route_name')
def home():
    return 'This is the home page'
