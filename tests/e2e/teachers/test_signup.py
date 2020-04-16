import requests
import json

# curl -i -X POST localhost:5000/user/signup -d '{"username": "teacher1@email.com", "password": "password1"}' --header "Content-Type: application/json"

API_ADDRESS = "http://flask-api-server:5000"

USERNAME = "teacher1@email.com"
PASSWORD = "password2"

def test_signup():
    url =  API_ADDRESS + '/user/signup'
    
    headers = {'Content-Type': 'application/json' } 
    payload = {'username': USERNAME, 'password': PASSWORD}

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 200

    responsePayload = response.json()
    assert responsePayload["uid"] is not None
    assert responsePayload['username'] == USERNAME