from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input'].lower()
    response = ""
    options = []
    link = ""

    if user_input == 'know more about redferns tech':
        response = "RedFerns Tech is a leading technology solutions provider specializing in Salesforce consultancy, Zoho services, ServiceNow implementation, and Data Science solutions."
    elif user_input == 'our services':
        response = "Please choose from the following service areas:"
        options = ["Salesforce", "Zoho", "Data Science and Machine Learning", "ITSM Tools ServiceNow"]
    elif user_input == 'salesforce':
        response = "Salesforce Services: \nImplementation \nCustomization \nIntegration \nSupport"
        options = ["Integration", "App Development", "Admin & Support", "Migration", "Key Solutions"]
    elif user_input == 'zoho':
        response = "Zoho Services:\nImplementation\nCustomization\nTraining Sessions"
        options = ["Zoho CRM", "Zoho Books", "Zoho Projects", "Zoho Analytics"]
    elif user_input == 'odoo':
        response = "Details about Odoo services..."
    elif user_input == 'itsm tools servicenow':
        response = "ServiceNow Implementation:\nEnd-to-End Implementation\nCustom App Development\nIT Service Management\nSupport"
    elif user_input == 'data science and machine learning':
        response = "Data Science Solutions:\nData Analysis\nPredictive Modeling\nMachine Learning\nData Visualization"
        options = ["Data Science", "Machine Learning"]
    elif user_input == 'our products':
        response = "Explore our innovative apps:"
        options = ["Currency Conversion App", "Mass Approvals App", "Thumbnail Viewer App", "Product Filter App"]
    elif user_input == 'currency conversion app':
        response = "Currency Conversion App:\nReal-time Currency Conversion\nMulti API Integration\nMulti Currency Support\nUser Friendly Interface\nReliable and Accurate\nEnhanced Reporting"
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=6d605bd9de3c-49d3-9fa4-ec3caabd5d63"
    elif user_input == 'mass approvals app':
        response = "Mass Approvals App:\nEffortless Approval Management\nStreamlined Approvals\nSimplify Approvals\nBoost Productivity\nSeamless Integration\nCustomization"
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=e671f4fe92fb476099e57a5df5754cfe"
    elif user_input == 'thumbnail viewer app':
        response = "Thumbnail Viewer App:\nVisual Delight for Files and Images\nImmersive Visual Experience\nStreamlined Content Management\nBlazing Fast Performance\nEffortless File and Image Upload"
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=3473ffd3d530462f828fd2c69f80d89d"
    elif user_input == 'product filter app':
        response = "Product Filter App:\nSimplify Salesforce Product Searches with Precision Filtering\nTailored Search Results\nSeamless Integration\nAdvanced Filtering Options\nBoosted Productivity"
        link = "https://appexchange.salesforce.com/appxListingDetail?listingId=cf4b19d4866749f783b0d2bc4032527b"
    elif user_input == 'career opportunities':
        response = "Click the link for career opportunities at RedFerns Tech."
        link = "https://redfernstech.com/careers/"
    else:
        response = "I'm sorry I didn't understand that. Please choose from the options above."

    return jsonify(response=response, options=options, link=link)

if __name__ == '__main__':
    app.run(debug=True)
