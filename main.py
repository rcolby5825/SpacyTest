# This is a sample Python script.
from http.server import HTTPServer, BaseHTTPRequestHandler

import spacy
import requests

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# port = 3005


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    # logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    # if len(argv) == 2:
    #     run(port=int(argv[1]))
    # else:
    run()


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# nlp = spacy.load("en_core_web_sm")
# doc1 = nlp("Apple is looking at buying U.K. startup for $1 billion.")
# print(doc1)
# # Iterate over tokens in a Doc
#
# for token in doc1:
#     # Print the text and the predicted part-of-speech tag
#     # predictive part of this may not be needed
#     print({"text": token.text, "pos": token.pos_, "predictive": token.head.text})
#     print(token)
#     # for ent in doc1.ents:
#     #     print(ent.text, ent.label_)
#
# i = 0
# while i < len(doc1):
#     # print(i)
#     print("lemma", doc1[i].lemma_)
#     print("POS", doc1[i].tag_)
#     print("dependencies?", doc1[i].dep_)
#     i += 1
#
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion in the Spring to Autumn.")
#
# for ent in doc.ents:
#     print(ent.text, ent.label_)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
