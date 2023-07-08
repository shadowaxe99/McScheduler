class Agent:
    def __init__(self, assistant):
        self.assistant = assistant

    def perform_task(self, task):
        return self.assistant.handle_task(task)