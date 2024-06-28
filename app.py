from flask import Flask, request, jsonify
from gradio_client import Client

# Initialize Flask app
app = Flask(__name__)

# Initialize Gradio client with your model's API endpoint
client = Client("srinukethanaboina/ME")

# Dictionary to store chat history
chat_history = {}

# Define endpoint for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the JSON data from the POST request
        data = request.json
        
        if not data:
            return jsonify({'error': 'No data received'}), 400
        
        # Extract query from JSON data
        query = data.get('queryResult', {}).get('queryText', '')
        
        if not query:
            return jsonify({'error': 'No query found in request'}), 400

        # Perform prediction using Gradio client
        result = client.predict(
            query=query,
            api_name="/predict"  # Replace with your model's endpoint
        )

        # Memorize the conversation
        memorize_conversation(query, result)

        # Return the result as JSON response
        return jsonify({'fulfillmentText': result})
    
    except Exception as e:
        # Log the error
        app.logger.error(f"Error processing webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Function to memorize conversation
def memorize_conversation(query, response):
    if query in chat_history:
        chat_history[query].append(response)
    else:
        chat_history[query] = [response]

# Define a simple route to test if the Flask app is running
@app.route('/')
def index():
    return "Flask app is running!"







