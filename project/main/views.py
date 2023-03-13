from flask import render_template
from flask_login import current_user
from flask_login import login_required


@main_blueprint.route('/')
def home():
    return render_template('main/index.html', current_user=current_user)
