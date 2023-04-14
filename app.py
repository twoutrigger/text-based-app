from utils.person import Person
from steps.get_name import get_name
from steps.get_phone import get_phone

def get_response(msg):
    return "Hi"




if __name__ == "__main__":

    bot_string = "Chatbot: "

    p = Person('', '')

    print("Let's get started! (type 'quit' to exit)")
    print("\n")
    print(bot_string + "What is your name?")

    while True:
        sentence = input("You: ")

        if sentence == "quit":
            break

        if p.person_name == '':
            collect_name = get_name(sentence)

            if collect_name:
                p.person_name = collect_name
                print(bot_string + "Thank you, " + collect_name)

            else:
                print(bot_string + "Sorry I didn't catch that. What is your name?")

        if p.phone_number == '':
            print(bot_string + "What is your phone number?")
            collect_phone = get_phone(sentence)

        # resp = get_response(sentence)
        # print(bot_string + resp)