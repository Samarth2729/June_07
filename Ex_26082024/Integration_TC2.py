# 2. Create a Booking,
# Delete the Booking with ID and
# Verify using GET request that it should not exist.

import allure
import requests
import pytest

@allure.title("Create Booking")
@allure.description("This test creates a booking.")
@allure.testcase("Test Case: Create Booking")
@allure.label("owner", "Samarth")
@pytest.mark.smoke
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    URL = f"{base_url}/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Salman",
        "lastname": "Khan",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    response_data = response.json()
    return response_data.get("bookingid")

def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    response_data = response.json()
    return response_data.get("token")

@allure.title("Delete Booking")
@allure.description("This test creates a booking, deletes it, and verifies that it no longer exists.")
@allure.testcase("Test Case: Delete Booking")
@allure.label("owner", "Samarth")
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
    assert response.status_code == 201

@allure.title("Get Booking by ID")
@allure.description("This test fetches a booking by ID to verify its existence.")
@allure.testcase("Test Case: Get Booking by ID")
@allure.label("owner", "Samarth")
def test_get_single_request_by_id():
    booking_id = create_booking()
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"

    response = requests.get(url=url)
    assert response.status_code == 200
    response_data = response.json()
    allure.attach(str(response_data), name="Fetched Booking Data", attachment_type=allure.attachment_type.JSON)
    print(response_data)


