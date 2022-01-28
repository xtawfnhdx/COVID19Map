from flask import Flask, render_template, url_for
from COVID19Map.db.dbInit import db
from COVID19Map.controller import co_bp
from COVID19Map.controller import st_bp
import WebAppConfig

app = Flask(__name__)
app.config.from_object(WebAppConfig)
db.init_app(app)
app.register_blueprint(co_bp)
app.register_blueprint(st_bp)


# db.create_all()


@app.route('/test')
def Index():
    return "abc"


# @app.route('/statistics')
# def Index_log():
#     return render_template("Statistics/Index.html")


if __name__ == "__main__":
    # app.run(host="0.0.0.0")c
    s = [2, 3, 4, 5, 6, 7]
    for x in range(len(s)):
        print(x)
