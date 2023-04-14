import spacy

nlp = spacy.load("en_core_web_sm")

def get_name(msg):

    doc = nlp(msg)

    name = False

    for entity in doc.ents:

        if entity.label_ == 'PERSON':

            name = entity.text
    
    return name
