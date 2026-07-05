from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FormPage:
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_TEXT = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.fields = {
            "first-name": "Надежда",
            "last-name": "Гриднева",
            "postal-code": "346398"
        }

    def get_form(self):
        for name, value in self.fields.items():
            field = self.wait.until(EC.presence_of_element_located(
                (By.ID, name)
            ))
            field.send_keys(value)

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def check_total(self):
        total = self.wait.until(EC.visibility_of_element_located(self.TOTAL_TEXT)).text
        assert total == "Total: $58.29"
