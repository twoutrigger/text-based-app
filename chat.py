from utils.person import Person
from steps.get_name import get_name
from steps.get_phone import get_phone
from steps.get_item import get_item
# from steps.next_step import next_step

def next_step(person, msg):

    repeat_prompt = "Sorry I didn't catch that. Please re-enter."

    if msg == None:
        prompt = "What is your name?"

    elif person.person_name == None:
        collect_name = get_name(msg)

        if collect_name:
            person.person_name = collect_name
            prompt = f"Thank you {collect_name}! And what is your phone number?"
        else:
            prompt = repeat_prompt
        
    elif person.phone_number == None:
        collect_phone = get_phone(msg)

        if collect_phone:
            person.phone_number = collect_phone
            prompt = f"Great! Your number is {collect_phone}. And what items do you need?"
        else:
            prompt = repeat_prompt

    elif person.item == None:
        collect_item = get_item(msg)

        if collect_item:
            person.item = collect_item

            item_str = "Thanks, you items are: "
            for k, v in collect_item.items():
                item_str += ('\n' + str(v) + ' ' + str(k))

            item_str += "\n\n(type 'quit' to exit)"

            prompt = item_str
        else:
            prompt = repeat_prompt

    prompt = "Chatbot: " + prompt

    return prompt


if __name__ == "__main__":

    person = Person(None, None, None)
    sentence = None

    print("Let's get started! (type 'quit' to exit)")
    print("\n")

    while True:

        print(next_step(person, sentence))

        sentence = input("You: ")

        if sentence == "quit":
            break