from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ShoppingPage:
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]

    def add_products(self):
       for product in self.products:
            add_button = f"add-to-cart-{product}"
        # print(add_button)
            self.driver.find_element(By.ID, add_button).click()

    def get_shopping_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART)).click()
