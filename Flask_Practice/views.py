#Run pip install flask-blueprint
from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/views')
def home():
    return render_template("index.html")


