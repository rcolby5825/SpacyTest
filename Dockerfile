FROM python:3.5-slim

MAINTAINER rcolby1313 <rachael.colby@dharbor.com>

#ENV LANG             en
#ENV SPACY_VERSION    3.4.4

RUN mkdir -p /usr/venv
COPY . /usr/venv/

RUN apt-get update
RUN apt-get install -y build-essential python-dev git

RUN pip3 install --upgrade pip setuptools

########################################
# spaCy
########################################
#RUN pip3 install spacy==${SPACY_VERSION}
RUN pip3 install spacy
#RUN python3 -m spacy.${LANG}.download all
RUN python3 -m spacy download en_core_web_sm

# Check whether the model was successfully installed
#RUN python3 /usr/spacy/test/load_lang.py
###################

WORKDIR /usr/venv
COPY main.py .

CMD ["python3", "main.py"]
