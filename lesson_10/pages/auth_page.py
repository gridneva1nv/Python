from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import allure


class AuthPage:
    """
    Класс представляет сущность "Авторизация на странице"

    У класса есть адрес сайта магазина, имя пользователя, пароль пользователя
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(self.driver, 10)
        self.username = "standard_user"
        self.password = "secret_sauce"

    def open(self) -> None:
        with allure.step(f"Открыть страницу {self.url}"):
            self.driver.get(self.url)

    def login(self) -> None:
        with allure.step(f"Ввести имя пользователя: {self.username}"):
            self.wait.until(EC.presence_of_element_located(
                self.USERNAME_INPUT
            )).send_keys(self.username)

        with allure.step(f"Ввести пароль пользователя: {self.password}"):
            self.wait.until(EC.presence_of_element_located(
                self.PASSWORD_INPUT
            )).send_keys(self.password)

        with allure.step("Нажать кнопку 'Авторизация'"):
            button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
            button.click()
