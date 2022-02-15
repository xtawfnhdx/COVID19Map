from flask import Blueprint, render_template, request, g, url_for, redirect, jsonify
from COVID19Map.db.model.TCountryMapping import TCountryMapping, TCountryTest
from COVID19Map.db.dbInit import db

#import threading

bp = Blueprint("COVID19", __name__, url_prefix='/')


@bp.route("/")
def index():
    # db.drop_all()
    # db.create_all()
    # admin = TCountryMapping('admin', 'admin@example.com')
    # guest = TCountryMapping('guest', 'guest@example.com')
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()

    # t1=TCountryTest("abc")
    # t2=TCountryTest("bbb")
    # db.session.add(t1)
    # db.session.add(t2)
    # db.session.commit()

    # 验证链接结果，判断是否可以正常链接数据库
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())

    coulist = TCountryMapping.query.all()
    # 基于结果的删除操作
    # TCountryMapping.query.all().delete()
    # coulist[0].delete()
    for x in coulist:
        print(x.FUID)
        print(x)
        # x.Fiso2=x.Fiso2+"t"
        # 执行删除操作
        # db.session.delete(x)
    db.session.commit()
    return render_template("COVID19/Index.html")
