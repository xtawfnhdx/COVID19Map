from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request,
    g)
from flask_migrate import Migrate
from COVID19Map.db.dbInit import db
from COVID19Map.controller import co_bp
from COVID19Map.controller import st_bp
from COVID19Map import WebAppConfig

app = Flask(__name__)
app.config.from_object(WebAppConfig)
db.init_app(app)
app.register_blueprint(co_bp)
app.register_blueprint(st_bp)

migrate = Migrate(app, db)


# db.drop_all()
# db.create_all()

@app.route('/test')
def Index():
    print('进来了')
    user_id = request.args.get("id")
    if user_id:
        return "有用户ID"
    else:
        return redirect(url_for("Index"))


# 所有请求之前的统一调用
@app.before_request
def test():
    print("钩子函数进来了")

    # setattr(g, "test", "abc")
    # 两种方式都可
    g.test = "ttt"


# 所有请求之后返回结果之前的调用
@app.context_processor
def context_after():
    print("调用之后的调用")


# @app.route('/statistics')
# def Index_log():
#     return render_template("Statistics/Index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    # s = [2, 3, 4, 5, 6, 7]
    # for x in range(len(s)):
    #    print(x)
