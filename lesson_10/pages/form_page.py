from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import allure


class FormPage:
    """
    Класс представляет сущность "Данные клиента"

    У класса есть браузер, время ожидания отображения страницы, данные для заполнения формы заказа: имя, фамилия, почтовый индекс
    """

    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_TEXT = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.fields = {
            "first-name": "Надежда",
            "last-name": "Гриднева",
            "postal-code": "346398"
        }

    @allure.step("Заполнить поля формы заказа")
    def get_form(self) -> None:
        with allure.step(f"Ввести данные в поля формы заказа: Имя - {self.fields['first-name']},"
                         f" Фамилия - {self.fields['last-name']}, Почтовый индекс - {self.fields['postal-code']}"):
            for name, value in self.fields.items():
                field = self.wait.until(EC.presence_of_element_located(
                    (By.ID, name)
                ))
                field.send_keys(value)

        with allure.step("Нажать кнопку 'Продолжить'"):
            self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def check_total(self) -> None:
        with allure.step("Получить стоимость заказа, находящегося в корзине"):
            total = self.wait.until(EC.visibility_of_element_located(self.TOTAL_TEXT)).text

        with allure.step("Сравнить полученную стоимость с ожидаемой"):
            assert total == "Total: $58.29"
