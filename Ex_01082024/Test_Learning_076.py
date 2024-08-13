# PUT Request
# URL
# Path - Booking id
# Payload
import requests
import pytest
import allure


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(url=url,headers=headers,json=json_payload)
    token = response.json()["token"]
    print(token)
    return token

def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)# Positional Parameters
    print(type(URL))
    print(type(headers))
    print(type(payload))

    assert response.status_code == 200
    responseData = response.json()
    booking_id = responseData["bookingid"]
    return booking_id

def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking())
    put_url = base_url+base_path
    cookie = f"token={create_token()}"
    headers = {"Content-Type": "application/json'"}

    payload = {
        "firstname": "Sammu",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=put_url,headers=headers,json=payload)
    assert response.status_code == 200
    responsedata = response.json()
    assert responsedata["firstname"] == "Sammu"
# Optionally, call the function to execute the test
test_put_request_positive()







