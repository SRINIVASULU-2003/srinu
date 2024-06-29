from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Store conversation history globally (for simplicity, consider using a database in production)
conversation_history = {}

# Define endpoint for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the JSON data from the POST request
        data = request.json
        
        if not data:
            return jsonify({'error': 'No data received'}), 400
        
        # Extract session ID from the request
        session_id = data.get('session', '')
        
        if not session_id:
            return jsonify({'error': 'No session ID found in request'}), 400
        
        # Extract query text from the request
        query_text = data.get('queryResult', {}).get('queryText', '')
        
        if not query_text:
            return jsonify({'error': 'No query text found in request'}), 400
        
        # Append query text to conversation history
        if session_id not in conversation_history:
            conversation_history[session_id] = []
        
        conversation_history[session_id].append(query_text)

        # Perform prediction using Gradio (example using mock predict function)
        result = predict_with_gradio(session_id)

        # Return the result as JSON response
        return jsonify({'fulfillmentText': result})
    
    except Exception as e:
        # Log the error
        app.logger.error(f"Error processing webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Mock function to simulate Gradio prediction
def predict_with_gradio(session_id):
    # Example: You might send the entire conversation history to Gradio
    history = conversation_history.get(session_id, [])
    
    # Perform prediction logic with Gradio based on history (replace with actual Gradio logic)
    # Here, we mock by returning the last query in the history
    if history:
        return history[-1]
    else:
        return "No conversation history available."

# Define a simple route to test if the Flask app is running
@app.route('/')
def index():
    return "Flask app is running!"


