from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import allure


class CalcPage:
    """
    Класс представляет сущность "Калькулятор"

    У класса есть адрес сайта, последовательность кнопок для ввода
    арифметичекого выражения, значение ожидаемого результат вычислений, время задержки вывода результата
    """

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    DELAY_TIME = 45
    SCREEN_OUTPUT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DELAY_TIME)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.keys = ["7", "+", "8", "="]
        self.result = "15"

    def open(self) -> None:
        with allure.step(f"Перейти на страницу {self.url}"):
            self.driver.get(self.url)

    @allure.step(f"Ввести время задержки вывода результата = {DELAY_TIME}")
    def delay(self) -> None:
        delay_field = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_field.clear()
        delay_field.send_keys(f"{self.DELAY_TIME}")

    def click_keys(self) -> None:
        for key in self.keys:
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//span[text() = '{key}']")
            )).click()

    def check_result(self) -> None:
        with allure.step("Измерить время до момента отображения результата вычисления"):
            start = time.perf_counter()
            self.wait.until(EC.text_to_be_present_in_element(
                self.SCREEN_OUTPUT, self.result
            ))
            timer = time.perf_counter() - start

        with allure.step("Сравнить время вывода результата с заданным"):
            assert int(timer) == self.DELAY_TIME
