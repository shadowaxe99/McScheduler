from utils import Utils
from voice import VoiceSupport

class Assistant:
    def __init__(self, ai_support, email_support, call_support):
        self.ai_support = ai_support
        self.email_support = email_support
        self.call_support = call_support
        self.utils = Utils()
        self.voice_support = VoiceSupport()

    def handle_task(self, task):
        if task['type'] == 'conversation':
            return self.ai_support.handle_user_input(task['input'])
        elif task['type'] == 'email':
            email = self.utils.parse_email(task['email'])
            return self.email_support.send_email(email['to'], email['subject'], email['body'])
        elif task['type'] == 'call':
            call = self.utils.parse_call(task['call'])
            return self.call_support.make_call(call['number'], call['message'])
        elif task['type'] == 'voice':
            text = self.voice_support.speech_to_text()
            return self.ai_support.handle_user_input(text)
        elif task['type'] == 'text_to_speech':
            return self.voice_support.text_to_speech(task['text'])
        elif task['type'] == 'email_to_speech':
            email = self.utils.parse_email(task['email'])
            return self.voice_support.text_to_speech(email['body'])
        elif task['type'] == 'email_and_call':
            email = self.utils.parse_email(task['email'])
            call = self.utils.parse_call(task['call'])
            email_response = self.email_support.send_email(email['to'], email['subject'], email['body'])
            call_response = self.call_support.make_call(call['number'], call['message'])
            return email_response + '\n' + call_response
        elif task['type'] == 'advanced_conversation':
            # TODO: Implement advanced conversation functionality
            pass
        else:
            return 'Unknown task type'