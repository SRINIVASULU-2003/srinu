from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input'].lower()
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
        response = ("Salesforce Services:\n- Implementation\n- Customization\n- Integration\n- Support\n"
                    "Explore our key solutions for more details:")
        #options = ["Sales Cloud Implementation", "Service Cloud Setup", "Custom Application Development", 
         #          "Salesforce Training", "Data Migration and Cleanup", "Experience Cloud Development",
            #       "Salesforce Analytics and Reporting", "Salesforce CPQ"]
    elif user_input == 'zoho':
        response = ("Zoho Services:\n- Implementation\n- Customization\n- Training Sessions\n"
                    "Choose a specific Zoho service to learn more:")
       # options = ["Zoho CRM", "Zoho Books", "Zoho Projects", "Zoho Analytics"]
    elif user_input == 'odoo':
        response = "Details about Odoo services..."
    elif user_input == 'itsm tools - servicenow':
        response = ("ServiceNow Implementation:\n- End-to-End Implementation\n- Custom App Development\n"
                    "- IT Service Management\n- Support")
    elif user_input == 'data science and machine learning':
        response = ("Data Science Solutions:\n- Data Analysis\n- Predictive Modeling\n- Machine Learning\n"
                    "- Data Visualization\nChoose an area to explore further:")
        options = ["Data Science", "Machine Learning"]
    elif user_input == 'our products':
        response = "Explore our innovative apps:"
        options = ["Currency Conversion App", "Mass Approvals App", "Thumbnail Viewer App", "Product Filter App"]
    elif user_input == 'currency conversion app':
        response = ("Currency Conversion App:\n- Real-time Currency Conversion\n- Multi API Integration\n"
                    "- Multi Currency Support\n- User Friendly Interface\n- Reliable and Accurate\n"
                    "- Enhanced Reporting")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=6d605bd9de3c-49d3-9fa4-ec3caabd5d63"
    elif user_input == 'mass approvals app':
        response = ("Mass Approvals App:\n- Effortless Approval Management\n- Streamlined Approvals\n"
                    "- Simplify Approvals\n- Boost Productivity\n- Seamless Integration\n- Customization")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=e671f4fe92fb476099e57a5df5754cfe"
    elif user_input == 'thumbnail viewer app':
        response = ("Thumbnail Viewer App:\n- Visual Delight for Files and Images\n- Immersive Visual Experience\n"
                    "- Streamlined Content Management\n- Blazing Fast Performance\n- Effortless File and Image Upload")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=3473ffd3d530462f828fd2c69f80d89d"
    elif user_input == 'product filter app':
        response = ("Product Filter App:\n- Simplify Salesforce Product Searches with Precision Filtering\n"
                    "- Tailored Search Results\n- Seamless Integration\n- Advanced Filtering Options\n"
                    "- Boosted Productivity")
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=cf4b19d4866749f783b0d2bc4032527b"
    elif user_input == 'career opportunities':
        response = "Click the link for career opportunities at RedFerns Tech."
        link = "https://redfernstech.com/careers/"
    elif user_input == 'chatwith':
        return redirect('/chatbot')
    else:
        response = "we will update it."

    return jsonify(response=response, options=options, link=link)

if __name__ == '__main__':
    app.run(debug=True)
