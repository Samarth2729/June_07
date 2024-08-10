import allure
import pytest
import requests
@allure.title("Create Booking Curd")
@allure.description("TC#2 -> Verify booking is not created with {} data")
@pytest.mark.curd
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)  # Positional Parameters
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 500

@allure.title("Create Booking Curd")
@allure.description("TC#3 -> Verify booking with totalprice string negative")
@pytest.mark.curd
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "Samarth",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    responseData = response.json()
    totalprice = responseData["booking"]["totalprice"]
    assert totalprice == 111

    # Assertions
    response.status_code == 200
