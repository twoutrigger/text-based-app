from utils.person import Person
from steps.get_name import get_name

def get_response(msg):
    return "Hi"




if __name__ == "__main__":

    p = Person('', '')

    print("Let's get started! (type 'quit' to exit)")
    print("\n")
    print("What is your name?")

    while True:
        sentence = input("You: ")

        if p.person_name == '':
            collect_name = get_name(sentence)

            if collect_name:
                p.person_name = collect_name
                print("Thank you, " + collect_name)

        if sentence == "quit":
            break

        resp = get_response(sentence)
        print("Chatbot:" + resp)