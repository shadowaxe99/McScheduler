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
    return flask.jsonify(message='This is a new endpoint')

@app.route('/task1')
def task1():
    return flask.jsonify(message='Task 1 endpoint')

@app.route('/task2')
def task2():
    return flask.jsonify(message='Task 2 endpoint')

@app.route('/task3')
def task3():
    return flask.jsonify(message='Task 3 endpoint')

if __name__ == '__main__':
    app.run(port=5001)