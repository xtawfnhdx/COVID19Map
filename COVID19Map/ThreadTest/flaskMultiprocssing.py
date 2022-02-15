from flask import Flask
from concurrent.futures import ProcessPoolExecutor
import json
import time


app = Flask(__name__)


def readTestA():
    time.sleep(0.1)
    return "testa"


def readTestB():
    time.sleep(0.2)
    return "testb"


def readTestC():
    time.sleep(0.3)
    return "testc"


@app.route("/")
def index():
    testa = pool.submit(readTestA)
    testb = pool.submit(readTestB)
    testc = pool.submit(readTestC)

    return json.dumps({
        "testa": testa.result(),
        "testb": testb.result(),
        "testc": testc.result()
    })


#
#
# @app.route("/")
# def index():
#     testa = readTestA()
#     testb = readTestB()
#     testc = readTestC()
#
#     return json.dumps({
#         "testa": testa,
#         "testb": testb,
#         "testc": testc
#     })


if __name__ == "__main__":
    pool = ProcessPoolExecutor()
    app.run()
