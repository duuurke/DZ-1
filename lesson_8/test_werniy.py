import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"
@pytest.fixture 

def get_token():
    token = "kcA6rdyshZoUgbUhtjdUKBw1DrJE2YGXFFl8qEpemZQOSFI-PMU+bQdwGh9dR+SV"
    return token 
    # headers = {'Content-Type': 'application/json'}
    # body = {
    # "login": "garaninserega7@gmail.com",
    # "password": "CFLWSH854kjTR86FEW8",
    # "companyId": "fba9e275-c019-42ba-b540-2803b577bffc"
    # }  
    # response = requests.post(base_url+"/auth/keys", headers=headers, json=body)
    # return response.json()['key']

def test_produce(get_token):
    he = {
    "Content-Type": "application/json", 
    "Authorization": f"Bearer {get_token}"
    }
    rest = requests.get(base_url+'/projects', headers=he)
    assert rest.status_code == 200

def test_create_project(get_token):
    he = {
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {get_token}"
        }
    body = {
        "title": "проект dz4.",
        "users": {"7f5a9548-a400-4cf9-9eb2-ab7740ed0a02": "admin"}
        }
    response = requests.post(base_url+"/projects", headers=he, json=body)

    assert response.status_code == 201
    id = requests.get(base_url+"/projects/" + response.json()['id'], headers=he).json()['id']
    assert id == response.json()['id']

def test_change_data(get_token):
    he = {
    "Content-Type": "application/json", 
        "Authorization": f"Bearer {get_token}"
     }
    body = {
        "title": "проект dz4.",
        "users": {"7f5a9548-a400-4cf9-9eb2-ab7740ed0a02": "admin"}
        }
    response = requests.post(base_url+"/projects", headers=he, json=body)
    body = {
    "title": "проект new"
    }
    response_change = requests.put(base_url+"/projects/" + response.json()['id'], headers=he, json=body)
    title = requests.get(base_url+"/projects/" + response.json()['id'], headers=he).json()["title"]
    assert title == "проект new"

def test_neg():
    he = {
        "Content-Type": "application/json"
        }
    body = {
        "title": "проект dz4.",
        "users": {"7f5a9548-a400-4cf9-9eb2-ab7740ed0a02": "admin"}
        }
    response = requests.post(base_url+"/projects", headers=he, json=body)

    assert response.status_code == 401
    