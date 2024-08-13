import requests
import pytest
import allure

def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
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
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    print(type(headers))
    print(type(payload))

    assert response.status_code == 200
    response_data = response.json()
    booking_id = response_data["bookingid"]
    return booking_id

def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    booking_id = create_booking()
    base_path = f"/booking/{booking_id}"
    put_url = base_url + base_path
    token = create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

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

    response = requests.put(url=put_url, headers=headers, json=payload)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["firstname"] == "Sammu"

# Optionally, call the function to execute the test
test_put_request_positive()


def test_delete_booking():
    base_url = "https://restful-booker.herokuapp.com"
    booking_id = create_booking()
    delete_url = f"{base_url}/booking/{booking_id}"

    token = create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    response = requests.delete(url=delete_url, headers=headers)

    # Assert that the delete request was successful
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Optionally, you can add more checks here to confirm that the booking was actually deleted


# Optionally, call the function to execute the test
test_delete_booking()

