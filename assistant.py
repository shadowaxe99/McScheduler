class Assistant:
    def __init__(self, ai_support, email_support, call_support):
        self.ai_support = ai_support
        self.email_support = email_support
        self.call_support = call_support

    def handle_task(self, task):
        if task['type'] == 'conversation':
            return self.ai_support.handle_user_input(task['input'])
        elif task['type'] == 'email':
            return self.email_support.send_email(task['to'], task['subject'], task['body'])
        elif task['type'] == 'call':
            return self.call_support.make_call(task['number'], task['message'])
        else:
            return 'Unknown task type'