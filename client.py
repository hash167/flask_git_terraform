import requests
import json

url = "http://localhost:8080/deploy"
data = {
    "name": "terraform",
    "branch": "main"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Request succeeded:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}:")
    print(response.text)
