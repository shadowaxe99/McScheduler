import flask
from conversational_ai_model import ConversationalAIModel
from conversational_ai_support import ConversationalAISupport

app = flask.Flask(__name__)

ai_model = ConversationalAIModel('placeholder_model_id')
ai_support = ConversationalAISupport(ai_model)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/new_endpoint')
def new_endpoint():
    return 'This is a new endpoint'

if __name__ == '__main__':
    app.run(port=5001)