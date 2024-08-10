import allure
import pytest
import requests

@allure.title("Test GET Request - Restful Booker Project#1")
@allure.description("TC#3 -> Verify that GET Request with ID works")
@allure.label("owner","Samarth")
@allure.tag("regression","P0","Smoke")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    assert responseData.status_code == 200

