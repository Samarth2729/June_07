import allure
import requests
import pytest

# 5. Invalid Creation - enter a wrong payload or Wrong JSON
@allure.title("#TC5 - Invalid creation with wrong payload or wrong JSON")
def test_invalid_creation():

        print("Create Booking Testcase")
        URL = "https://restful-booker.herokuapp.com/booking"
        headers = {"Content-Type": "application/json"}
        json_payload = {}
        response = requests.post(url=URL, headers=headers, json=json_payload)
        # Assertions
        assert response.status_code == 500