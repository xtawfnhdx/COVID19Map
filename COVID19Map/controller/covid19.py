from flask import Blueprint, render_template, request, g, url_for, redirect
from COVID19Map.db.model.TCountryMapping import TCountryMapping
from COVID19Map.db.dbInit import db

bp = Blueprint("COVID19", __name__, url_prefix='/')


@bp.route("/")
def index():
    # admin = TCountryMapping('admin', 'admin@example.com')
    # guest = TCountryMapping('guest', 'guest@example.com')
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    coulist = TCountryMapping.query.all()
    for x in coulist:
        print(x)
    return render_template("COVID19/Index.html")
