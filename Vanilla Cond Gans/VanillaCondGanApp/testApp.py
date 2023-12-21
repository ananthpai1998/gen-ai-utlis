import requests
import json


url = "http://localhost:5000/"

# Set the Content-Type header to application/json
headers = {'Content-Type': 'application/json'}

# Provide the user input as a dictionary and convert it to JSON
data = {'input': 4}
json_data = json.dumps(data)

# Make a POST request with JSON data
response = requests.post(url, data=json_data, headers=headers)

if response.status_code == 200:
    # Save the received image file
    with open('generated_image.png', 'wb') as f:
        print(response.content)
        f.write(response.content)
    print('Received image saved successfully as generated_image.png')
else:
    print(f'Request failed with status code: {response.status_code}')
    print(response.text)

