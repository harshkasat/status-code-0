import requests

# URL of your Flask API
api_url = "http://127.0.0.1:5000/generate"

# Input JSON data
input_data = {
    "input_text": "Precautions of High fever"
}

# Send a POST request with JSON payload
response = requests.post(api_url, json=input_data)

# Check if the request was successful
if response.status_code == 200:
    generated_text = response.json()["generated_text"]
    print("Generated Text:", generated_text)
else:
    print("Error:", response.text)
