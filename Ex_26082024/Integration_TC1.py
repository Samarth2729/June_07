import requests
import pytest
import allure

# Integration Scenarios
# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.

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
@allure.title("Create Booking")
@allure.description("This test creates a booking.")
@allure.testcase("Test Case: Create Booking")
@allure.label("owner","Samarth")
@pytest.mark.smoke
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

@allure.title("Positive Test for PATCH Request")
@allure.description("This test verifies that the PATCH request successfully updates booking details.")
@allure.label("owner", "Samarth")
@allure.testcase("Test Case: Partial Update Patch")
def test_patch_request_positive():
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
        "firstname": "Laila",
        "lastname": "Taylor",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.patch(url=put_url, headers=headers, json=payload)
    print("PATCH Request Response Status Code:", response.status_code)
    print("PATCH Request Response Body:", response.json())

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    response_data = response.json()
    assert response_data["firstname"] == "Laila"
    assert response_data["lastname"] == "Taylor"

# Optionally, call the function to execute the test
test_patch_request_positive()



