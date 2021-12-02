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

#
#
# @app.route('/')
# def Index():
#     return render_template("COVID19/Index.html")
#
#
# @app.route('/statistics')
# def Index_log():
#     return render_template("Statistics/Index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
