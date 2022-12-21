#Run pip install flask-blueprint
from flask import Blueprint, render_template, request, jsonify


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/profile')
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name = name)


@views.route('/json')
def get_json():
    return jsonify({'name':'Gero', 'coolness':10})

