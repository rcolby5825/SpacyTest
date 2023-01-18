import sys
import spacy
import json
import datetime

nlp = spacy.load("en_core_web_sm")
# nlp.enable_pipe("parser")
nlp.enable_pipe("senter")
# Construction via add_pipe with default model
# parser = nlp.add_pipe("parser")
# ner = nlp.add_pipe("ner")
t = []
e = []
d = []
lemma = ''

# print("Python %s on %s" % (sys.version, sys.platform))
def get_doc(name):
    # doc1 = nlp("Apple is looking at buying U.K. startup for $1 billion.")
    doc1 = nlp(name)
    # print(doc1)
    # Iterate over tokens in a Doc

    i = 0
    while i < len(doc1):
        # print(i)
        d.append({"lemma": doc1[i].lemma_, "POS": doc1[i].tag_, "dependencies?": doc1[i].dep_})
        # print("lemma", doc1[i].lemma_)
        # print("POS", doc1[i].tag_)
        # print("dependencies?:   ", doc1[i].dep_)
        # print("ent_type:   ", doc1[i].ent_type_)
        # print("sentiment:   ", doc1[i].sentiment)
        # print("ent_iob:   ", doc1[i].ent_iob_)
        # print("sent:   ", doc1[i].sent)

        i += 1
    return d


# sys.path.append("../../spacy")

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# gets named entities from the sentence (maybe able to combine with doc method)
# def get_entities(name):
#     doc = nlp(name)
#     for ent in doc.ents:
#         # print("ent_label: ", ent.label_)
#         # print("ent_text: ", ent.text)
#         e.append({"ent_label": ent.label_, "ent_text": ent.text})
#     return e


# gets tokens from the sentence
def get_tokens(name):
    global lemma
    doc2 = nlp(name)
    date = datetime.date.today()
    # print("\n Default Date Object:", date, "\n")
    formatted_date = datetime.date.strftime(date, "%m/%d/%Y")
    j = 0
    for token in doc2:
        # print("cluster: ", token)
        # print("bytes: ", bool(token.whitespace_))
        # print("c: ", token.c)
        # print("doc: ", token.sentiment)
        # print("lefts: ", token)
        lemma = lemma + token.lemma_ + token.whitespace_
        t.append({"index": j + 1, "word": token.text, "originalText": token.text, "tag": token.pos_,
                  "predictive": token.head.text, "length": token.__len__(),
                  "dep": token.dep_, "pos": token.tag_, "lemma": token.lemma_,
                  "ner": token.ent_type_,
                  "characterOffsetBegin": token.idx, "characterOffsetEnd": token.idx + token.__len__(),
                  "before": doc2[j - 1].whitespace_,
                  "after": token.whitespace_})
        if token.ent_type_.__len__() != 0:
            e.append({"ent_label": token.ent_type_, "ent_text": token.text})
            # print("ent_type: ", token.ent_type_)
            # print("offset_end: ", token.text)
        j += 1
        # print({"text": token.text, "pos": token.pos_,
        #        "predictive": token.head.text, "length": token.__len__(),
        #        "dependencies": token.dep_, "tag": token.tag_})
    print(
        json.dumps({"docDate": formatted_date, "sentence": name, "lemmaSentence": lemma, "sentences": [{"tokens": t}, {"named_entities": e}]}))
    return t, lemma
    # gives how long the token is

    # print("dep: ", token.dep_)
    # print("tag: ", token.tag_)
    # Print the text and the predicted part-of-speech tag
    # predictive part of this may not be needed
    # same as POS
    # print("ancestors: ", token.ancestors)
    # print("doc: ", token.__doc__)
    # for ent in doc1.ents:
    #     print(ent.text, ent.label_)


def print_sentence(name):
    date = datetime.date.today()
    # print("\n Default Date Object:", date, "\n")
    formatted_date = datetime.date.strftime(date, "%m/%d/%Y")
    # Use a breakpoint in the code line below to debug your script.
    # print(json.dumps({"sentence": name}))  # Press Ctrl+F8 to toggle the breakpoint.
    get_tokens(name)
    # get_entities(name)
    get_doc(name)
    # print('lemma' + lemma)
    # print(
    #     json.dumps({"docDate": formatted_date, "sentence": name, "lemmaSentence": lemma, "sentences": [{"tokens": t}, {"named_entities": e}]}))
    # print(json.dumps({"named_entities": e}))


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_sentence(sys.argv[1])
    # print(sys.argv[1])
    # j = json.loads(sys.argv[1]) #sys.argv[0] is filename
    # print(j)
