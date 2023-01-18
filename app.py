from flask import Flask, render_template
from waitress import serve
import json

import main

app = Flask(__name__)


@app.route('/')
def hello_world():
    main.testcase()
    print(main.t)
    return render_template("index.html"), json.dumps(main.t)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8085)
