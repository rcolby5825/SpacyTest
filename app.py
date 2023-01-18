from flask import Flask
from waitress import serve
import json

import main

app = Flask(__name__)


@app.route('/')
def hello_world():
    main.testcase()
    print(main.t)
    return json.dumps(main.t)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8085)
