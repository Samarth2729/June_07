# 3. Get an Existing Booking id from Get All Bookings Ids ,
# Update a Booking and Verify using GET by id
import allure
import requests
import pytest
import random

import requests
import random
import allure


def get_all_booking_ids():
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url)
    assert response.status_code == 200
    bookings = response.json()
    return [booking['bookingid'] for booking in bookings]

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


def update_booking(booking_id, token):
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    payload = {
        "firstname": "UpdatedFirstName",
        "lastname": "UpdatedLastName",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-02"
        },
        "additionalneeds": "None"
    }
    response = requests.put(url, headers=headers, json=payload)
    assert response.status_code == 200
    return response.json()


def get_booking_by_id(booking_id):
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    response = requests.get(url)
    assert response.status_code == 200
    return response.json()


@allure.title("Update Booking and Verify")
@allure.description("This test updates an existing booking and verifies the update by retrieving the booking by ID.")
@allure.label("owner", "your_name")  # Replace with your name or identifier
@allure.label("environment", "test")  # Adjust based on your environment
@allure.testcase("https://your_jira_or_tracker_url/testcase_id")  # Optional: Link to a testcase in a tracker
def test_update_and_verify_booking():
    # 1. Get all booking IDs
    booking_ids = get_all_booking_ids()
    assert booking_ids, "No bookings found"

    # Randomly select a booking ID
    booking_id = random.choice(booking_ids)

    # Create a token (assuming this function is defined elsewhere)
    token = create_token()

    # 2. Update the selected booking
    update_booking(booking_id, token)

    # 3. Verify the update by retrieving the booking by ID
    booking = get_booking_by_id(booking_id)

    assert booking["firstname"] == "UpdatedFirstName"
    assert booking["lastname"] == "UpdatedLastName"
    assert booking["totalprice"] == 200
    assert booking["depositpaid"] is False
    assert booking["bookingdates"]["checkin"] == "2024-01-01"
    assert booking["bookingdates"]["checkout"] == "2024-01-02"
    assert booking["additionalneeds"] == "None"


# Optionally, call the function to execute the test
test_update_and_verify_booking()
