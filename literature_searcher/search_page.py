from flask import Blueprint, render_template

bp = Blueprint("search_page", __name__)

@bp.route("/")
def index():
    return render_template("search_page.html")
