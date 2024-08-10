import allure
import pytest
import requests

@allure.title("Test GET Request - Restful Booker Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.label("owner","Samarth")
@allure.tag("regression","P0","Smoke")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    print(responseData.text)
    assert responseData.status_code == 200

@allure.title("Test GET Request - Restful Booker Project#1")
@allure.description("TC#2 -> Verify that GET Request with Invalid ID")
@allure.label("owner","Samarth")
@allure.tag("regression","P0","Smoke")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_negative_id():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert responseData.status_code == 404
