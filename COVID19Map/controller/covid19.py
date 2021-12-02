from flask import Blueprint, render_template, request, g, url_for, redirect
from COVID19Map.db.model import TCountryMapping

bp = Blueprint("COVID19", __name__, url_prefix='/')


@bp.route("/")
def index():
    # coulist = TCountryMapping.query.all()
    return render_template("COVID19/Index.html")
