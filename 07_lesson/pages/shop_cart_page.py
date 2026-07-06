from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCart:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ORDER_LIST = (By.CLASS_NAME, "cart_list")
    ORDER_ITEM = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def get_order(self):
        self.wait.until(EC.visibility_of_element_located(self.ORDER_LIST))
        return self.driver.find_elements(*self.ORDER_ITEM)

    def checkout_click(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()