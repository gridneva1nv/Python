from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import allure


class ShoppingPage:
    """
        Класс представляет сущность "Магазин"

        У класса есть список товаров для добавления в корзину
        """

    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]

    def add_products(self) -> None:
        with allure.step(f"Добавить в корзину товары из списка {self.products}"):
            for product in self.products:
                add_button = f"add-to-cart-{product}"
                self.driver.find_element(By.ID, add_button).click()

    @allure.step('Нажать кнопку "Корзина"')
    def get_shopping_cart(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART)).click()
