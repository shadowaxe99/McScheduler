# McScheduler

McScheduler is a conversational AI project. Its primary purpose is to create an AI assistant that can interact with users, handle emails, and make automated calls. The project is now in the development phase, and many functionalities are being implemented.

## Detailed File Structure and Descriptions

The project is composed of several Python files, each serving a specific purpose:

- main.py: This is the entry point of the application. It creates an instance of the ConversationalAIModel with a placeholder model ID, and an instance of ConversationalAISupport using the AI model. It then enters a loop to continually accept user input and generate responses.

- conversational_ai_model.py: This file contains the ConversationalAIModel class. The class currently serves as a placeholder for a more complex AI model. The generate_response method simply echoes user input.

- conversational_ai_support.py: This file contains the ConversationalAISupport class. This class uses the ConversationalAIModel to generate responses to user input.

- email_handling_support.py: This file contains the EmailHandlingSupport class. This class has methods for sending and reading emails, both currently implemented as placeholders.

- automated_calls_support.py: This file contains the AutomatedCallsSupport class. The class has a method for making automated calls, which is currently implemented as a placeholder.

- assistant.py: This file contains the Assistant class, which is intended to serve as the main class for handling tasks. Currently, it is a placeholder file and needs to be developed further.

- agent.py: This file is intended to represent a human agent that can interact with the assistant. It's currently a placeholder file.

- voice.py: This file is intended to convert text to speech and speech to text. It's currently a placeholder file.

- utils.py: This file is intended to hold utility functions that can be used across the project. It's currently a placeholder file.

## Detailed Instructions on How to Run the Application

In its current state, you can interact with the application by running the main.py script and typing input into the console. Here's how you can do this:

1. Open a terminal.
2. Navigate to the directory containing main.py.
3. Run the command python main.py.
4. Once the script is running, you can type input into the console and press Enter to see the response.

## Future Work and Contributions

As this project is now in the development stages, there's a lot of room for development and improvement. Here are a few areas where contributions would be particularly useful:

- Implement the ConversationalAIModel using a real AI model, such as OpenAI's GPT-3.
- Develop the EmailHandlingSupport class to send and read emails using libraries like smtplib, imaplib, or poplib.
- Develop the AutomatedCallsSupport class to make automated calls using an API from a service like Twilio or Plivo.
- Expand the Assistant class to handle a variety of tasks using the support classes.
- Implement the Agent class to interact with the Assistant in an interesting and useful way.
- Develop the VoiceSupport class to convert text to speech and speech to text.

If you want to contribute, please fork this repository, make your changes, and create a pull request.

## License

This project is licensed under the MIT License.