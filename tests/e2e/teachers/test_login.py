import requests
import json

from config import API_ADDRESS
from randomize.randomString import randomString
from randomize.randomEmail import randomEmail

# curl -i -X POST localhost:5000/user/login -d '{"username": "teacher1@email.com", "password": "password1"}' --header "Content-Type: application/json"

USERNAME = randomEmail()
PASSWORD = randomString()

def test_login():
    headers = {'Content-Type': 'application/json' } 

    # Signup

    signupUrl =  API_ADDRESS + '/user/signup'
    
    payload = {'username': USERNAME, 'password': PASSWORD}

    response = requests.post(signupUrl, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 200

    # Login

    loginUrl =  API_ADDRESS + '/user/login'
    
    payload = {'username': USERNAME, 'password': PASSWORD}

    response = requests.post(loginUrl, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 200

    responsePayload = response.json()
    assert responsePayload["access_token"] is not None

def test_negative_login():
    headers = {'Content-Type': 'application/json' } 

    # Login

    loginUrl = API_ADDRESS + '/user/login'
    
    payload = {'username': randomEmail(), 'password': randomString()}

    response = requests.post(loginUrl, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 400