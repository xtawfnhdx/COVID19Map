from flask import Flask, render_template, url_for

from COVID19Map.controller.studentshow import emp
import WebAppConfig

app = Flask(__name__)
app.config.from_object(WebAppConfig)


# app.register_blueprint(emp)


@app.route('/')
def Index():
    return render_template("COVID19/Index.html")


@app.route('/statistics')
def Index_log():
    return render_template("Statistics/Index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
