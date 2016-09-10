from flask import Blueprint, render_template
from flask_security import login_required

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
@login_required
def index():
    return "ELF API"    
