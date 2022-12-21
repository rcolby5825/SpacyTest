# Spacy Test Module

### Installation



### Table of Contents

  - [Release Notes](#release-notes)
- [Installation](#installation)
- [NLU Plugins](#nlu-plugins)
  - [City](#city)
  - [Date](#date)
  - [Duration](#duration)
  - [Emoji](#emoji)
  - [Icon](#icon)
  - [Location](#location)
  - [Money](#money)
  - [Number](#number)
  - [OpenIE](#openie)
  - [Ordinal](#ordinal)
  - [Organization](#organization)
  - [Percent](#percent)
  - [Person](#person)
  - [Quoted](#quoted)
  - [State or Province](#state-or-province)
  - [Time](#time)
- [Chunkers](#chunkers)
  - [Adjective](#adjective)
  - [Adverb](#adverb)
  - [Conjunction](#conjunction)
  - [Example](#example)
  - [Modal Verb](#modal-verb)
  - [Noun](#noun)
- [Services Overview](#services-overview)
  - [NLU Parser](#nlu-parser)
  - [Structured Content Parser](#structured-content-parser)
  - [NER Service](#ner-service)
- [FAQ](#FAQ)
- [Versioning](#versioning)
  - [History](#history)
  - [Convention](#convention)
  - [Release cycle](#release-cycle)
- [License](#license)


### NLU Plugins
 * CITY
 * DATE              Absolute or relative dates or periods                               "July 4, 1776", "February", "next Tuesday"              {tid: "t1", type: "DATE", value: "1776-07-04"}
 ** DURATION          Time period                                                         "2 hours"                                               {tid: "t1", type: "DURATION", value: "PT2H"}
 * EMOJI             Call out to get emoji for token
 * ICON              Call out to get icon for token
 * LOCATION          Countries, cities, states, mountain ranges, bodies of water         "Boston", "Rocky Mountains"
 * MONEY             Monetary values, including unit                                     "$1,000"                                                $1000.0
 * NUMBER            Number                                                              "123"                                                   123.0
 * OPENIE            Relationships between person and object                             "John goes to the zoo"                                  OpenIE [
 *                                                                                                                                                           {
 *                                                                                                                                                               "subject": "John",
 *                                                                                                                                                               "subjectSpan": [0, 1],
 *                                                                                                                                                               "relation": "goes to",                                                                                                                                                               "relationSpan": [1, 3],
 *                                                                                                                                                               "object": "zoo",                                                                                                                                                              "objectSpan": [4, 5]
 *                                                                                                                                                       ]
 * ORDINAL           Ordinal number, including "first", "second", etc                    "First"                                                 1.0
 * ORGANIZATION      Companies, agencies, institutions, etc                              "Digital Harbor"
 * PERCENT           Percentage, including "%"                                           "100%"                                                  %100
 * PERSON            People, including fictional                                         "Reagan"
 * QUOTED
 * STATEORPROVINCE
 * TIME             Times smaller than a day, duration, recurring events                "2 pm"                                                  {tid: "t1", type: "TIME", value: "2021-01-13T14:00"}

### City
```sh
        let socialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.City, this.getLocation.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback for location.
     * 
     * @param name - name of location
     * @result
     */
     getLocation(text: string, packet?: string): any;
```

### Date
```sh
        let socialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Date, this.getDate.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to pass date.
     * 
     * @param name - name of icon
     * @result name and color of icon
     */
     getDate(text: string, packet?: string): any;
```

### Duration
```sh
        let socialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Duration, this.getDuration.bind(this));
```

Example call-back function:

```sh

    /**
     * Callback to pass tag (#tag).
     * 
     * @param name - name of icon
     * @result name and color of icon
     */
     getDuration(text: string, packet?: string): any;
```

### Emoji
```sh
        let socialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Emoji, this.getEmoji.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback for emoji.
     * 
     * @param name - name of emoji
     * @result
     */
     getEmoji(text: string, packet?: string): any;
```

### Icon
```sh
        let socialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Icon, this.getIcon.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to supply name and color for icon.
     * 
     * @param name - name of icon
     * @result name and color of icon
     */
    getIcon(text: string, packet?: string): any;
```

### Location
```sh
       let socialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Location, this.getLocation.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback for location.
     * 
     * @param name - name of location
     * @result
     */
     getLocation(text: string, packet?: string): any;
```

### Money
```sh
        let socialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Money, this.getMoney.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to pass money.
     * 
     * @param name - name of icon
     * @result name and color of icon
     */
     getMoney(text: string, packet?: string): any;
```

### Number
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Number, this.getNumber.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to pass number.
     * 
     * @param name - number text
     * @result name and color of icon
     */
     getNumber(text: string, packet?: string): any;
```

### OpenIE
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.OpenIE, this.setOpenIE.bind(this));
        socialService.addEventListener(Type.OpenIEObject, this.setObject.bind(this));
        socialService.addEventListener(Type.OpenIESubject, this.setSubject.bind(this));
        socialService.addEventListener(Type.OpenIERelation, this.setRelation.bind(this));
```

Example call-back functions:

```sh
    /**
     * Callback to pass OpenIE packet.
     * 
     * @param text - OpenIE packet
     * @result undefined
     */
    setOpenIE(text: string, packet?: string): any;

    /**
     * Callback to pass OpenIE object.
     * 
     * @param text - OpenIE object
     * @result undefined
     */
     setObject(tokens: any[], openie: string): any;

    /**
     * Callback to pass OpenIE subject.
     * 
     * @param text - OpenIE subject
     * @result undefined
     */
     setSubject(tokens: any[], openie: any): any;rn undefined;
    }

    /**
     * Callback to pass OpenIE relation.
     * 
     * @param text - OpenIE relation
     * @result undefined
     */
  setRelation(tokens: any[], openie: any): any;
```

### Ordinal
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Ordinal, this.getOrdinal.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to pass ordinal.
     * 
     * @param text - ordinal
     * @result name and color of ordinal
     */
     getOrdinal(text: string, packet?: string): any;
```

### Organization
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Organization, this.getOrganization.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback for organization.
     * 
     * @param text - name of organization
     * @result
     */
     getOrganization(text: string, packet?: string): any;
```

### Percent
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Percent, this.getPercent.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to pass percent.
     * 
     * @param text - percent text
     * @result name and color of percent
     */
     getPercent(text: string, packet?: string): any;
```

### Person
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Person, this.getPerson.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback for person.
     * 
     * @param text - name of person
     * @result to be documented
     */
     getPerson(text: string, packet?: string): any;
```

### Quoted
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Quote, this.getQuoted.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to supply URL for quoted text.
     * 
     * @param name - quoted text
     * @result URL for click of quoted text
     */
    getQuoted(text: string, packet?: string): any;
```

### State or Province
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.StateOrProvince, this.getLocation.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback for state or province.
     * 
     * @param name - name of location
     * @result to be documented
     */
     getLocation(text: string, packet?: string): any;
```
### Time
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Time, this.getTime.bind(this));
```

Example call-back function:

```sh
    /**
     * Callback to pass time.
     * 
     * @param name - time text
     * @result name and color of time
     */
     getTime(text: string, packet?: string): any;
```

### Chunkers
 * ADJECTIVE         Comparitors with optional conjunctions               "greater or equal"         
 * ADVERB
 * CONJUNCTION       Words used to connect clauses or sentences           "and", "but"
 * EXAMPLE           Content to be displayed in popover                   "I like the zoo [Try Hogle zoo]."
 * MODALVERB         State of object                                      "should be", "will be"
 * NN                People, places, or things. Includes acronyms         "President", "Reagan", "Liberty", "mountain", "IRS"

### Adjective
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        let nluParser = serviceAccessor.getService(Services.NLU);
        socialService.addEventListener(Type.Adjective, this.getPacket.bind(this));

        // Add adjective, such as <greater than>
        nluParser.addChunkHandler({
            rules: { ner: Type.Adjective, startsWith: ['JJ', 'JJR'], contains: ['CC', 'IN'], endsWith: ['JJ', 'JJR', 'IN'] },
            tags: { color: 'red' }
        });
```

Example call-back function:

```sh
    /**
     * Callback to pass visual attributes.
     * 
     * @param name - text
     * @result visual attributes
     */
     getPacket(text: string, packet?: string): any;
```

### Adverb
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        let nluParser = serviceAccessor.getService(Services.NLU);
        socialService.addEventListener(Type.Adverb, this.getPacket.bind(this));

        // Add adverb, such as <will do>
        nluParser.addChunkHandler({
            rules: { ner: Type.Adverb, startsWith: ['RB'], contains: ['RB'], endsWith: ['RB'] },
            tags: { startTag: '<strong>', endTag: '</strong>', caps: true }
        })
```

Example call-back function:

```sh
    /**
     * Callback to pass adverb chunker text.
     * 
     * @param name - adverb text
     * @result visual attributes
     */
     getPacket(text: string, packet?: string): any;
```

### Conjunction
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        let nluParser = serviceAccessor.getService(Services.NLU);
        socialService.addEventListener(Type.Conjunction, this.getPacket.bind(this));

        // Add conjunction, such as "this <and> that"
        nluParser.addChunkHandler({
            rules: { ner: Type.Conjunction, startsWith: ['CC'], contains: ['CC'], endsWith: ['CC'] },
            tags: { color: 'red' }
        })
```

Example call-back function:

```sh
    /**
     * Callback to conjunction text.
     * 
     * @param name - conjunction text
     * @result visual attributes
     */
     getPacket(text: string, packet?: string): any;
```

### Example
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        let nluParser = serviceAccessor.getService(Services.NLU);
        socialService.addEventListener(Type.ModalVerb, this.getPacket.bind(this));

        // Add out comment, such as "For example [see wikipedia]."
        nluParser.addChunkHandler({
            rules: { ner: 'Example', startsWith: ['-LRB-'], endsWith: ['-RRB-'] },
            tags: { score: 1 }
        })
```

Example call-back function:

```sh
    /**
     * Callback to pass example text.
     * 
     * @param name - example text
     * @result visual attributes
     */
     getPacket(text: string, packet?: string): any;
```

### Modal Verb
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        let nluParser = serviceAccessor.getService(Services.NLU);
        socialService.addEventListener(Type.ModalVerb, this.getPacket.bind(this));

        // Add modal verb, such as <will do>
        nluParser.addChunkHandler({
            rules: { ner: Type.ModalVerb, startsWith: ['MD'], contains: ['MD', 'VB'], endsWith: ['VB'] },
            tags: { color: 'red' }
        })
```

Example call-back function:

```sh
    /**
     * Callback to pass modal verb text.
     * 
     * @param text - modal verb text
     * @result visual attributes
     */
     getPacket(text: string, packet?: string): any;
```

### Noun
```sh
        let socialService: SocialService = serviceAccessor.getService(Services.SocialService);
        socialService.addEventListener(Type.Noun, this.getNounTag.bind(this));

        // Add noun, such as "My <liability insurance> expired."
        let nluParser = serviceAccessor.getService(Services.NLU);
        nluParser.addChunkHandler({
            rules: { ner: 'NN', startsWith: ['NN', 'NNP'], contains: ['NN', 'NNP'], endsWith: ['NN', 'NNP'] },
            tags: { color: 'blue' }
        })
```

Example call-back function:

```sh

    /**
     * Callback to pass noun text.
     * 
     * @param name - moun text
     * @result visual attributes
     */
     getNounTag(text: string, packet?: string): any;
```

### Services Overview

The Social Text component given access to a variety of services. These services include:

1. TextParser - Helper functions for parsing DOM content
2. NLU Parser - Natural Language Understanding processing
3. Listener Service - Voice Listener service
4. Social Service - Allows listeners to be registered with Social Text
5. Attribute Utils - Utilities for processing text attributes
6. Popup Service - Popup utilities
7. Toolbar Service - Toolbar utilities for adding toolbar items
8. Template Service - Template utilities
9. Smart Text base class - For adding references, mentions, actions, tags, etc
10. NER Service - Service to recognize named entities specified by client solution

Access to services is provided when the Social Text is initialized. The following example shows how to access the Social Service.

```sh
  let serviceAccessor = socialTextBootstrap();
  let socialService = serviceAccessor.getService('SocialService');
```

### NLU Parser

The NLU Parser service allows html to be processed by Natural Language Processing server.

Service name is 'NLUParser' or CallbackServices.NLUParser.

```sh
    /**
     * Add rules, tags, or directives for new chunk processors.
     * 
     * For example:
     *       this.addChunkHandler({
     *          rules: { ner: 'Adjective', startsWith: ['JJ', 'JJR'], contains: ['CC', 'IN'], endsWith: ['JJ', 'JJR', 'IN'] },
     *          tags: { color: 'red' }
     *      });
     * 
     * @param handlerPacket - JSON structure
     */
    addChunkHandler(handlerPacket: any): void;

    /**
     * Process text with Natural Language Processor, and call NER and other callbacks.
     * 
     * @param textToProcess textToProcess
     * @returns html of processing results
     */
    async processNLU(textToProcess: string);

    /**
     * Fetch results from Natural Language Processor.
     * 
     * @param content - HTML content to be processed
     * @param editorCapabilities - limitations in host HTML tag
     * @returns JSON with NLP results
     */
    public async fetchNLUResults(content: string, editorCapabilities?: any);
```

### Social Service

### Attribute Utils

### Structured Content Parser

Use the Structured Content Parser to populate parameters based on NLU Named Entities.

```sh
    /**
     * Populate structure rules.
     * 
     * @param sentenceData - NLU JSON representing parsed sentence
     * @param structure - structure to be populated, for ex, '[PERSON][JIRA][DATE][TIME]'
     * @returns populated structure, for ex, '[PERSON:Rohit|Scott][JIRA:SC-123][DATE:1 pm tomorrow(T13:00 OFFSET P1D)][TIME:?]'
     */
    getParams(sentenceData: any, structure: string): string;
```

### Card Service


### NER Service

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


