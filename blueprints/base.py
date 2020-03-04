from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

base = Blueprint('base', __name__, template_folder='templates')

@base.route('/', defaults={'page': 'index'})
@base.route('/')
def index():
    return render_template('index.html')

@base.route('/icons')
def icons():
    return render_template('icons.html')