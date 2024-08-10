import allure
import pytest
import requests


# To make Request
# URL
# Method >>> Post
# Headers >> Content - Type>Application/JSON
# Authentication >> No
# Payload > body , data >> Dict/ JSON

@allure.title("Create Booking Curd")
@allure.description("TC#1 -> Verify create booking")
@pytest.mark.curd
def test_create_booking_positive_tc1():
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
    response = requests.post(url=URL, headers=headers, json=payload)  # Positional Parameters
    assert response.status_code == 200
    responseData = response.json()

    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert isinstance(responseData["bookingid"], int)
    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    checkout = "2019-01-01"



