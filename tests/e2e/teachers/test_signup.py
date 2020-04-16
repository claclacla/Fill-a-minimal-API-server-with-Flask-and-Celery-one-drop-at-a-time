import requests
import json

from config import API_ADDRESS
from randomize.randomString import randomString
from randomize.randomEmail import randomEmail

# curl -i -X POST localhost:5000/user/signup -d '{"username": "teacher1@email.com", "password": "password1"}' --header "Content-Type: application/json"

USERNAME = randomEmail()
PASSWORD = randomString()

def test_signup():
    url =  API_ADDRESS + '/user/signup'
    
    headers = {'Content-Type': 'application/json' } 
    payload = {'username': USERNAME, 'password': PASSWORD}

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 200

    responsePayload = response.json()
    assert responsePayload["uid"] is not None
    assert responsePayload['username'] == USERNAME

def test_signup_check_if_exists():
    url =  API_ADDRESS + '/user/signup'
    
    headers = {'Content-Type': 'application/json' } 
    payload = {'username': randomEmail(), 'password': randomString()}

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 200

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 400

def test_signup_with_invalid_email_address():
    url =  API_ADDRESS + '/user/signup'
    
    headers = {'Content-Type': 'application/json' } 
    payload = {'username': 'invalid_email_address', 'password': PASSWORD}

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 400

def test_signup_with_empty_payload():
    url =  API_ADDRESS + '/user/signup'
    
    headers = {'Content-Type': 'application/json' } 
    payload = {}

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 400

def test_signup_without_username():
    url =  API_ADDRESS + '/user/signup'
    
    headers = {'Content-Type': 'application/json' } 
    payload = {'password': PASSWORD}

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 400

def test_signup_without_password():
    url =  API_ADDRESS + '/user/signup'
    
    headers = {'Content-Type': 'application/json' } 
    payload = {'username': USERNAME}

    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
    assert response.status_code == 400