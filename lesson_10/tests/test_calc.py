import pytest
from selenium import webdriver
from pages.calc_page import CalcPage
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.severity("Critical")
@allure.id("Calc-1")
@allure.description("Проверка времени вывода результата вычисления на примере 7+8=15")
@allure.feature("READ")
@allure.title("Тестирование калькулятора с отсрочкой вывода результата")
def test_calc_page(driver):
    with allure.step("Перейти на страницу калькулятора"):
        calc = CalcPage(driver)
        calc.open()
    with allure.step("Указать время задержки вывода результата"):
        calc.delay()
    with allure.step("Нажать кнопки для вычисления выражения"):
        calc.click_keys()
    with allure.step("Получить результат вычислений"):
        calc.check_result()
