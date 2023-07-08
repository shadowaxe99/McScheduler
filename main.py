from conversational_ai_support import ConversationalAISupport
from conversational_ai_model import ConversationalAIModel
from email_handling_support import EmailHandlingSupport
from automated_calls_support import AutomatedCallsSupport
from assistant import Assistant
from agent import Agent
from voice import VoiceSupport

def main():
    ai_model = ConversationalAIModel('gpt-3.5-turbo')
    ai_support = ConversationalAISupport(ai_model)
    email_support = EmailHandlingSupport('your_email@gmail.com', 'your_password')  # Replace with your email and password
    call_support = AutomatedCallsSupport('your_account_sid', 'your_auth_token')  # Replace with your Twilio account SID and auth token
    voice_support = VoiceSupport()
    assistant = Assistant(ai_support, email_support, call_support)
    agent = Agent(assistant)

    while True:
        user_input = voice_support.speech_to_text()
        task = {'type': 'conversation', 'input': user_input}
        response = agent.perform_task(task)
        voice_support.text_to_speech(response)

if __name__ == '__main__':
    main()