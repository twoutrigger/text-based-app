from utils.person import Person
from steps.get_name import get_name
from steps.get_phone import get_phone
from steps.get_item import get_item

def get_response(msg):
    return "Hi"


if __name__ == "__main__":

    bot_string = "Chatbot: "

    p = Person('', '', '')

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

            if collect_phone:
                p.phone_number = collect_phone
                print(bot_string + "Thanks, you number is " + collect_phone)

            else:
                print(bot_string + "Sorry I didn't catch that. What is your phone number?")

        if p.item == '':
            print(bot_string + "What items do you need today?")
            collect_item = get_item(sentence)

            if collect_item:
                p.item = collect_item
                print(bot_string + "Thanks, you items are:")
                print(collect_item)
                print(type(collect_item))

                for k, v in collect_item.items():
                    print(str(v) + ' ' + str(k))

            else:
                print(bot_string + "Sorry I didn't catch that. What items do you need today?")



        # resp = get_response(sentence)
        # print(bot_string + resp)

        ## need to change the loop structure, since get_phone is prompted right after entering get_name