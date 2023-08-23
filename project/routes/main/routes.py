from flask import render_template
from project.routes.main import bp

@bp.route("/")
def index():
    return render_template('/users/login.html')
