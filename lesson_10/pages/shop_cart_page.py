from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import allure


class ShoppingCart:
    """
    Класс представляет сущность "Корзина"

    У класса есть список товаров ранее размещеных в корзине
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")
    ORDER_LIST = (By.CLASS_NAME, "cart_list")
    ORDER_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]                              # исходный список покупок

    def get_order(self) -> None:
        with allure.step("Получить список товаров, находящихся в корзине"):
            self.wait.until(EC.visibility_of_element_located(self.ORDER_LIST))
            cards = self.driver.find_elements(*self.ORDER_ITEM)
            names = []              # список для текста из карточек
            for card in cards:
                name = card.text    # извлечение текста из карточки
                names.append(name)  # добавление элемента в список
        with allure.step("Сравнить список товаров, находящихся в корзине с исходным списком товаров"):
            assert names == self.items

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def checkout_click(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
