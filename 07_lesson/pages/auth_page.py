from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(self.driver, 10)
        self.username = "standard_user"
        self.password = "secret_sauce"

    def open(self):
        self.driver.get(self.url)

    def login(self):
        self.wait.until(EC.presence_of_element_located(
            self.USERNAME_INPUT
        )).send_keys(self.username)

        self.wait.until(EC.presence_of_element_located(
            self.PASSWORD_INPUT
        )).send_keys(self.password)

        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()
