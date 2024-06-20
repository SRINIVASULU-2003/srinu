from flask import Flask, request, jsonify
from gradio_client import Client

# Initialize Flask app
app = Flask(__name__)

# Initialize Gradio client
client = Client("https://c818f6f0883afa8779.gradio.live")

# Define endpoint for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the POST request
    data = request.json
    
    # Extract query from JSON data
    query = data.get('query', '')

    # Perform prediction using Gradio client
    
    result = client.predict(
		query=query,
		api_name="/predict"
    )

    # Return the result as JSON response
    return jsonify(result=result)

# Define a simple route to test if the Flask app is running
@app.route('/')
def index():
    return "Flask app is running!"

# Run the Flask app



