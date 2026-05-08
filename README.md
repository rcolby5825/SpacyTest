# Spacy NLP Service

### Description - 
    Runs Spacy Natural Languange Processing as a service. Created as an initial POC as a microservice to be backwards compatibility with Stanford NLP LLM by having the outputs be generated the same for the application programming interface (API).  

### Installation -
    To run flask development server run command - python3 -m flask run - Go to localhost:5000.
    To run production server run app script. - Waitress WSGI production server.
    To build docker image run command - docker build --tag {containernameinlowercasehere} .
    To run docker container - docker run --publish 8085:8085 {containernameinlowercasehere}

### Update Requirements
    To create and update the requirements.txt - use command - pip install pipreq


### Release Notes

| Version | Ticket | Fix |
| - | - | - |
| v2.2.21| SC-980 | After insert a Card in text area and then write something contentEditable=false is not respected  |


### FAQ

#### FAQ 1

#### FAQ 2

### Versioning

#### History

You can discover the version history and change logs on the
[Releases](https://github.com/primus/primus/releases) page

#### Convention


#### Release cycle

There isn't a steady or monthly release cycle. We usually release a new version
when:

1. A critical bug is discovered.
2. There have been a lot of minor changes.
3. A framework did an incompatible update.
4. A new framework is added.
5. People ask for it.

### License

This will remain empty for now - test run only

### Dev Mode

### Build


