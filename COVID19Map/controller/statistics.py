from flask import Blueprint, render_template, request, redirect

bp = Blueprint('statistics', __name__, url_prefix="/statistics")


@bp.route("/")
def index():
    return render_template("Statistics/Index.html")
