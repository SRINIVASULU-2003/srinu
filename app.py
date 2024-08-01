from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input', '').lower()  # Use get() to avoid KeyError
    response = ""
    options = []
    link = ""

    if user_input == 'know more about redferns tech':
        response = ("RedFerns Tech is a leading technology solutions provider specializing in "
                    "Salesforce consultancy, Zoho services, ServiceNow implementation, and Data Science solutions. "
                    "We are committed to delivering innovative and customized solutions to meet your business needs.")
    elif user_input == 'our services':
        response = "Please choose from the following service areas:"
        options = ["Salesforce", "Zoho", "Data Science and Machine Learning", "ITSM Tools - ServiceNow"]
    elif user_input == 'salesforce':
        response = ("Salesforce Services:\nImplementation\nCustomization\nIntegration\nSupport\n"
                    "Explore our key solutions for more details:")
        options = ["menu"]
    elif user_input == 'zoho':
        response = ("Zoho Services:\nImplementation\nCustomization\nTraining Sessions\n"
                    "Choose a specific Zoho service to learn more:")
        options = ["menu"]
    elif user_input == 'odoo':
        response = "Details about Odoo services..."
        options = ["menu"]
    elif user_input == 'itsm tools - servicenow':
        response = ("ServiceNow Implementation:\n- End-to-End Implementation\n- Custom App Development\n"
                    "- IT Service Management\n- Support")
    elif user_input == 'data science and machine learning':
        response = ("Data Science Solutions:\nData Analysis\nPredictive Modeling\nMachine Learning\n"
                    "Data Visualization\nChoose an area to explore further:")
        options = ["Data Science", "Machine Learning"]
    elif user_input == 'our products':
        response = "Explore our innovative apps:"
        options = ["Currency Conversion App", "Mass Approvals App", "Thumbnail Viewer App", "Product Filter App"]
    elif user_input == 'currency conversion app':
        response = ("Currency Conversion App:\n- Real-time Currency Conversion\n- Multi API Integration\n"
                    "- Multi Currency Support\n- User Friendly Interface\n- Reliable and Accurate\n"
                    "- Enhanced Reporting")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000Is77CUAR"
        options = ["menu"]
    elif user_input == 'mass approvals app':
        response = ("Mass Approvals App:\n- Effortless Approval Management\n- Streamlined Approvals\n"
                    "- Simplify Approvals\n- Boost Productivity\n- Seamless Integration\n- Customization")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000K24EdUAJ"
        options = ["menu"]
    elif user_input == 'thumbnail viewer app':
        response = ("Thumbnail Viewer App:\n- Visual Delight for Files and Images\n- Immersive Visual Experience\n"
                    "- Streamlined Content Management\n- Blazing Fast Performance\n- Effortless File and Image Upload")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000K8u1dUAB"
        options = ["menu"]
    elif user_input == 'product filter app':
        response = ("Product Filter App:\n- Simplify Salesforce Product Searches with Precision Filtering\n"
                    "- Tailored Search Results\n- Seamless Integration\n- Advanced Filtering Options\n"
                    "- Boosted Productivity")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000K23xNUAR"
        options = ["menu"]
    elif user_input == 'career opportunities':
        response = "Click the link for career opportunities at RedFerns Tech."
        link = "https://redfernstech.com/careers/"
    elif user_input == 'menu':
        response = ("Hi! Welcome to RedFerns Tech! I'm FernAI, here to help you explore our innovative solutions and services.\n"
                    "Please select from below")
        options = ["Know more about RedFerns Tech", "Our services", "Our products", "Career opportunities", "Chat with an expert"]
    elif user_input == 'chatwith':
        return redirect('/chatbot')
    elif user_input == 'Chat with an expert':
        return redirect('/chatbot')
    else:
        response = "You can contact us and discuss using this link."
        link = "https://redfernstech.com/contact-us/"

    return jsonify(response=response, options=options, link=link)

if __name__ == '__main__':
    app.run(debug=True)
