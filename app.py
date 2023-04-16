from utils.person import Person
from steps.next_step import next_step

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