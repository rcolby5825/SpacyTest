from flask import Flask, render_template, request
from waitress import serve
import json
import main
import nlp_spacy_service

app = Flask(__name__)


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
    return render_template("index.html"), json.dumps(main.t)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8085)
