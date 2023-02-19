import requests
import json

def predict_top_gainer(stock_list):
    # Define the endpoint for the Hugging Face API
    endpoint = "https://api.huggingface.co/models/bert-base-uncased-finetuned-stock-prediction"

    # Define the header for the API request
    header = {
        "Content-Type": "application/json"
    }

    # Define the input data for the API request
    input_data = {
        "stock_list": stock_list
    }

    # Make a POST request to the Hugging Face API
    response = requests.post(endpoint, headers=header, data=json.dumps(input_data))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        result = json.loads(response.text)

        # Extract the top gainer from the result
        top_gainer = result["top_gainer"]

        # Return the top gainer
        return top_gainer
    else:
        # Return an error message
        return "Error: API request failed"
