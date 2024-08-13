# 4. Create a BOOKING, Delete It
import allure
import requests
import pytest

def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    URL = f"{base_url}/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Teja",
        "lastname": "Rao",
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