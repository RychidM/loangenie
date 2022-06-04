from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

