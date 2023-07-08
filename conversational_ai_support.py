from conversational_ai_model import ConversationalAIModel

class ConversationalAISupport:
    def __init__(self, ai_model):
        if isinstance(ai_model, ConversationalAIModel):
            self.ai_model = ai_model
        else:
            raise TypeError('ai_model must be an instance of ConversationalAIModel')

    def generate_response(self, user_input):
        return self.ai_model.generate_response(user_input)