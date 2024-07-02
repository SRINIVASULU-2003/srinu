from flask import Flask, request, jsonify
from gradio_client import Client
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize Gradio client
client = Client("srinuksv/SRUNU")  # Replace with your Gradio app name

# Dictionary to store conversation history
conversation_history = {}

# Define endpoint for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the JSON data from the POST request
        data = request.json
        if not data:
            return jsonify({'error': 'No data received'}), 400

        # Extract session ID and query from JSON data
        session_id = data.get('session')
        query = data.get('queryResult', {}).get('queryText', '')

        if not session_id:
            return jsonify({'error': 'No session ID found in request'}), 400
        
        if not query:
            return jsonify({'error': 'No query found in request'}), 400

        # Initialize the session history if not present
        if session_id not in conversation_history:
            conversation_history[session_id] = []

        # Add the query to the conversation history
        conversation_history[session_id].append(query)

        # Join the conversation history into a single string
        full_conversation = "\n".join(conversation_history[session_id])

        # Perform prediction using Gradio client
        result = client.predict(
            query=full_conversation,
            api_name="/predict"
        )

        # Add the result to the conversation history
        conversation_history[session_id].append(result)

        # Return the result as JSON response
        return jsonify({'fulfillmentText': result})
    
    except Exception as e:
        # Log the error
        app.logger.error(f"Error processing webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Define a simple route to test if the Flask app is running
@app.route('/')
def index():
    return "Flask app is running!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
