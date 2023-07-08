import flask
from conversational_ai_model import ConversationalAIModel
from conversational_ai_support import ConversationalAISupport

app = flask.Flask(__name__)

ai_model = ConversationalAIModel('placeholder_model_id')
ai_support = ConversationalAISupport(ai_model)

@app.route('/')
def home():
    user_input = input('Enter your input: ')
    response = ai_support.generate_response(user_input)
    return response

if __name__ == '__main__':
    app.run()