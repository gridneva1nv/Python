from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class CalcPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    DELAY_TIME = 45
    SCREEN_OUTPUT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DELAY_TIME)
        self.keys = ["7", "+", "8", "="]
        self.result = "15"

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self):
        delay_field = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_field.clear()
        delay_field.send_keys(f"{self.DELAY_TIME}")

    def click_keys(self):
        for key in self.keys:
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//span[text() = '{key}']")
            )).click()

    def check_result(self):
        start = time.perf_counter()
        self.wait.until(EC.text_to_be_present_in_element(
            self.SCREEN_OUTPUT, self.result
        ))
        timer = time.perf_counter() - start
        assert int(timer) == self.DELAY_TIME
