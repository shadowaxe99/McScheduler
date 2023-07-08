from conversational_ai_model import ConversationalAIModel

class ConversationalAISupport:
    def __init__(self, ai_model):
        self.ai_model = ai_model

    def generate_response(self, user_input):
        return self.ai_model.generate_response(user_input)