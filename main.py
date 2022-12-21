# This is a sample Python script.

import spacy


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

nlp = spacy.load("en_core_web_sm")
doc1 = nlp("This and not to see any money around or being spent this time of year.")
print(doc1)
#Iterate over tokens in a Doc
for token in doc1:
    # Print the text and the predicted part-of-speech tag
    # predictive part of this may not be needed
    print({"text": token.text, "pos": token.pos_, "predictive": token.head.text})


doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.label_)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
