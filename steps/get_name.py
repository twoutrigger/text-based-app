import spacy

nlp = spacy.load("en_core_web_sm")

text = "My name is Jim"

doc = nlp(text)

for entity in doc.ents:

    if entity.label_ == 'PERSON':
        print ('Person found')
        # save entity.text i.e. Jim

    else:
        print("Sorry I didn't get that")