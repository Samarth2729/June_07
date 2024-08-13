# 6. Trying to Update on a Delete Id -> 404
import requests
import random
import allure


# Function to get all booking IDs
def get_all_booking_ids():
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    try:
        bookings = response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Failed to decode JSON. Response text: {response.text}")
        raise
    return [booking['bookingid'] for booking in bookings]


# Function to delete a booking
def delete_booking(booking_id, token):
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    if response.headers.get('Content-Type') == 'application/json':
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON. Response text: {response.text}")
            raise
    else:
        return response.text


# Function to create an authentication token
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    try:
        token = response.json()["token"]
    except requests.exceptions.JSONDecodeError:
        print(f"Failed to decode JSON. Response text: {response.text}")
        raise
    return token


# Function to attempt updating a booking and expecting 405 Method Not Allowed
@allure.title("Update Deleted Booking")
@allure.description("This test tries to update a deleted booking and expects a 405 Method Not Allowed error.")
@allure.label("owner", "your_name")  # Replace with your name or identifier
@allure.label("environment", "test")  # Adjust based on your environment
def test_update_deleted_booking():
    # Get all booking IDs
    booking_ids = get_all_booking_ids()
    assert booking_ids, "No bookings found"

    # Randomly select a booking ID to delete
    booking_id = random.choice(booking_ids)

    # Create a token for authentication
    token = create_token()

    # Delete the selected booking
    delete_booking(booking_id, token)

    # Attempt to update the deleted booking
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    payload = {
        "firstname": "ShouldNotUpdate",
        "lastname": "ShouldNotUpdate",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-02-01",
            "checkout": "2024-02-02"
        },
        "additionalneeds": "None"
    }

    response = requests.patch(url, headers=headers, json=payload)
    print("Update Request Response Status Code:", response.status_code)
    print("Update Request Response Body:", response.text)

    # Check if the response status code is 405
    assert response.status_code == 405, f"Expected 405 but got {response.status_code}"


# Optionally, call the function to execute the test
test_update_deleted_booking()



