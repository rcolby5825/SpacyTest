from flask import Flask, render_template, request, make_response
from flask_cors import CORS
from waitress import serve
import json
import nlp_spacy_service
import config as cfg
app = Flask(__name__)

CORS(app)


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
    # getting input with name = fname in HTML form
        first_name = request.form.get("sentence")
        # display_data = find_element(, 'loginForm')
        # getting input with name = lname in HTML form
        #add async await here
        json_final = nlp_spacy_service.print_sentence(first_name)
        return json_final
    # main.testcase()
    # print(main.t)
    return render_template("index.html")


@app.route('/sentence', methods=["POST"])
def sentence():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json; charset=utf-8':
        nlp_obj = nlp_spacy_service.print_sentence(request.json['sentence'])
        return nlp_obj
    else:
        return 'Content-Type not supported!'


if __name__ == "__main__":
    serve(app, host=cfg.environment["host"], port=cfg.environment["port"])
