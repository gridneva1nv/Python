import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.shopping_page import ShoppingPage
from pages.shop_cart_page import ShoppingCart
from pages.form_page import FormPage
import allure


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.severity("Blocker")
@allure.id("Shop-1")
@allure.description("Проверка корректности добавления списка товаров в корзину"
                    " и расчета суммы заказа")
@allure.feature("READ")
@allure.title("Тестирование оформления заказа")
def test_shop(driver):
    with allure.step("Перейти на страницу магазина в браузере"):
        auth_page = AuthPage(driver)
        auth_page.open()
    with allure.step("Пройти авторизацию"):
        auth_page.login()
    with allure.step("Добавить товары в корзину"):
        shopping_page = ShoppingPage(driver)
        shopping_page.add_products()
        shopping_page.get_shopping_cart()
    with allure.step("Проверить список товаров в корзине"):
        shopping_cart = ShoppingCart(driver)
        shopping_cart.get_order()
        shopping_cart.checkout_click()
    with allure.step("Проверить стоимость заказа"):
        form_page = FormPage(driver)
        form_page.get_form()
        form_page.check_total()
