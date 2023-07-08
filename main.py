from conversational_ai_support import ConversationalAISupport
from conversational_ai_model import ConversationalAIModel
from email_handling_support import EmailHandlingSupport
from automated_calls_support import AutomatedCallsSupport
from assistant import Assistant
from agent import Agent

def main():
    ai_model = ConversationalAIModel('gpt-3.5-turbo')
    ai_support = ConversationalAISupport(ai_model)
    email_support = EmailHandlingSupport()
    call_support = AutomatedCallsSupport()
    assistant = Assistant(ai_support, email_support, call_support)
    agent = Agent(assistant)

    while True:
        user_input = input('> ')
        task = {'type': 'conversation', 'input': user_input}
        response = agent.perform_task(task)
        print(response)

if __name__ == '__main__':
    main()