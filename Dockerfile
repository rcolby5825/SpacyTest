FROM python:3.10.9
MAINTAINER rcolby1313 <rachael.colby@dharbor.com>

#ENV LANG='en'
#ENV SPACY_VERSION='3.4.0'
#ENV SPACY_MODEL='en_core_web_sm'

RUN mkdir -p /usr/venv
COPY . /usr/venv/

RUN apt-get update
RUN apt-get install -y build-essential python-dev git

#RUN pip3 install --upgrade pip setuptools

RUN pip install --upgrade pip setuptools

########################################
# spaCy
########################################
#Command is having issues - look into upgrading python
#RUN pip3 install 'spacy==${SPACY_VERSION}'
#CMd is not needed when adding the model
#RUN python3 -m spacy.${LANG}.download all
#Cmd works
COPY requirements.txt .

RUN pip install -r requirements.txt
#RUN pip3 install -r requirements.txt
##installing spacy seperately for now
#RUN pip3 install spacy
##RUN python3 -m spacy download en_core_web_sm
#RUN python3 -m spacy download ${SPACY_MODEL}

# Check whether the model was successfully installed
#RUN python3 /usr/spacy/test/load_lang.py
###################

WORKDIR /usr/venv
COPY main.py .

COPY app.py .

# CMD ["python3", "main.py"]
CMD ["python3", "app.py"]
