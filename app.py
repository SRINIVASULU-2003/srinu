from flask import Flask, request, jsonify, session
from flask_session import Session
from gradio_client import Client
import secrets
import hashlib

# Initialize Flask app
app = Flask(__name__)

# Configure SECRET_KEY and SESSION_TYPE
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generate a secure random key
app.config['SESSION_TYPE'] = 'filesystem'  # Use 'filesystem' for development

# Initialize Flask-Session
Session(app)

# Initialize Gradio client
client = Client("srinukethanaboina/ME")

def get_client_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        # In case of proxy, get the original client IP
        return request.environ['HTTP_X_FORWARDED_FOR']

def generate_session_id(ip_address):
    # Generate a unique session ID using the client's IP address
    return hashlib.sha256(ip_address.encode()).hexdigest()

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

        # Get the client's IP address
        client_ip = get_client_ip()
        
        # Generate a session ID based on the IP address
        session_id = generate_session_id(client_ip)
        
        # Set the session ID
        session['session_id'] = session_id
        
        # Retrieve conversation history from the session
        conversation_history = session.get(session_id, [])
        
        # Add the current query to the conversation history
        conversation_history.append(query)
        
        # Perform prediction using Gradio client
        result = client.predict(
            query={'history': conversation_history},
            api_name="/predict"
        )
        
        # Add the response to the conversation history
        conversation_history.append(result)
        
        # Save the updated conversation history back to the session
        session[session_id] = conversation_history

        # Return the result as JSON response for Dialogflow
        return jsonify({'fulfillmentText': result})
    
    except Exception as e:
        # Log the error
        app.logger.error(f"Error processing webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Define a simple route to test if the Flask app is running
@app.route('/')
def index():
    return "Flask app is running!"

