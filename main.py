
from conversational_ai_support import ConversationalAISupport
from conversational_ai_model import ConversationalAIModel

def main():
    ai_model = ConversationalAIModel("gpt-3.5-turbo")
    ai_support = ConversationalAISupport(ai_model)

    while True:
        user_input = input("> ")
        response = ai_support.handle_user_input(user_input)
        print(response)

if __name__ == "__main__":
    main()
    