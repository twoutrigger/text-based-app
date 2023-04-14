from models import person


def get_response(msg):
    return "Hi"

if __name__ == "__main__":
    print("Let's get started! (type 'quit' to exit)")
    print("\n")
    print("What is your name?")
    while True:
        sentence = input("You: ")

        if sentence == "quit":
            break

        resp = get_response(sentence)
        print("Chatbot:" + resp)