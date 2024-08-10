import pytest
import allure

@allure.title("TC1 - verify that 1-1 equal to 0")
@allure.description("This test verifies that the result of subtracting 1 from 1 is equal to 0")
@pytest.mark.smoke
def test_sub0():
    assert 1 - 1 == 0
@allure.title("TC2 - verify that 2-1 equal to 1")
@allure.description("This test verifies that the result of subtracting 1 from 2 is equal to 1")
@pytest.mark.regression
def test_sub1():
    assert 2 - 1 == 1
@allure.title("TC3 - verify that 3-1 equal to 2")
@allure.description("This test verifies that the result of subtracting 1 from 3 is equal to 2")
@pytest.mark.smoke
def test_sub2():
    assert 3 - 1 == 2
@allure.title("TC4 - verify that 4-1 equal to 3")
@allure.description("This test verifies that the result of subtracting 1 from 4 is equal to 3")
@pytest.mark.skip (reason="This test is skipped")
def test_sub3():
    assert 4 - 1 == 3
@allure.title("TC5 - verify that 5-1 equal to 4")
@allure.description("This test verifies that the result of subtracting 1 from 5 is equal to 4")
@pytest.mark.sanity
def test_sub4():
    assert 5 - 1 == 4
# pytest file path --alluredir=allure_result >>>>>>>>

