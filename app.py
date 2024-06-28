

import os
from flask import Flask, request, jsonify
from gradio_client import Client
import hashlib
import json

# Initialize Flask app
app = Flask(__name__)

# Initialize Gradio client with your model's API endpoint
client = Client("srinukethanaboina/ME")

# Directory to store conversation history
CONVERSATION_HISTORY_DIR = 'conversation_history'

# Ensure the directory exists
os.makedirs(CONVERSATION_HISTORY_DIR, exist_ok=True)

# Function to generate a unique user ID from session data
def generate_user_id(session_data):
    # Generate a unique hash for the session data
    session_hash = hashlib.sha256(json.dumps(session_data).encode()).hexdigest()
    return session_hash[:8]  # Return a shorter user ID for readability

# Function to load conversation history for a user
def load_conversation_history(user_id):
    history_file = os.path.join(CONVERSATION_HISTORY_DIR, f"{user_id}.txt")
    history = {}
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    query, response = line.split('|')
                    query = query.strip()
                    response = response.strip()
                    if query in history:
                        history[query].append(response)
                    else:
                        history[query] = [response]
    return history

# Function to save conversation history for a user
def save_conversation_history(user_id, history):
    history_file = os.path.join(CONVERSATION_HISTORY_DIR, f"{user_id}.txt")
    with open(history_file, 'w') as f:
        for query, responses in history.items():
            for response in responses:
                f.write(f"{query} | {response}\n")

# Define endpoint for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the JSON data from the POST request
        data = request.json
        
        if not data:
            return jsonify({'error': 'No data received'}), 400
        
        # Extract session data from JSON (assuming session data is available in 'session')
        session_data = data.get('session', {})
        
        # Generate a user ID based on session data
        user_id = generate_user_id(session_data)

        # Load conversation history for the user
        chat_history = load_conversation_history(user_id)

        # Extract query from JSON data
        query = data.get('queryResult', {}).get('queryText', '')
        
        if not query:
            return jsonify({'error': 'No query found in request'}), 400

        # Perform prediction using Gradio client
        result = client.predict(
            query=query,
            api_name="/predict"  # Replace with your model's endpoint
        )

        # Memorize the conversation for the user
        memorize_conversation(user_id, query, result, chat_history)

        # Return the result as JSON response
        return jsonify({'fulfillmentText': result})
    
    except Exception as e:
        # Log the error
        app.logger.error(f"Error processing webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Function to memorize conversation for a user
def memorize_conversation(user_id, query, response, chat_history):
    if query in chat_history:
        chat_history[query].append(response)
    else:
        chat_history[query] = [response]

    # Save updated conversation history for the user
    save_conversation_history(user_id, chat_history)

# Define a simple route to test if the Flask app is running
@app.route('/')
def index():
    return "Flask app is running!"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)




