import pytest
from selenium import webdriver
from pages.calc_page import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calc_page(driver):
    calc = CalcPage(driver)
    calc.open()
    calc.delay()
    calc.click_keys()
    calc.check_result()
