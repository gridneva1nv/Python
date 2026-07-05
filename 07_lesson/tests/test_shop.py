import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.shopping_page import ShoppingPage
from pages.shop_cart_page import ShoppingCart
from pages.form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.login()
    shopping_page = ShoppingPage(driver)
    shopping_page.add_products()
    shopping_page.get_shopping_cart()
    shopping_cart = ShoppingCart(driver)
    shopping_cart.get_order()
    shopping_cart.checkout_click()
    form_page = FormPage(driver)
    form_page.get_form()
    form_page.check_total()
