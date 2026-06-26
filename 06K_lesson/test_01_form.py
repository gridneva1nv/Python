from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color


def test_01_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 5)

    # 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html в Edge или Safari
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполните форму значениями:
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for name, value in form_data.items():
        field_value = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, f'[name="{name}"]')
        ))
        field_value.send_keys(value)

    # 3. Нажмите кнопку Submit
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "btn-outline-primary")
    ))
    submit_button.click()

    # 4. Проверьте, что поле Zip code подсвечено красным
    field_colour = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")
        )).value_of_css_property("background-color")
    field_colour_hex = Color.from_string(field_colour).hex

    assert field_colour_hex == "#f8d7da"

    # 5. Проверьте, что остальные поля подсвечены зеленым
    fields = {
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
        }
    for item in fields:
        field_colour = wait.until(EC.presence_of_element_located(
            (By.ID, item)
            )).value_of_css_property("background-color")
        field_colour_hex = Color.from_string(field_colour).hex
        assert field_colour_hex == "#d1e7dd"
    driver.quit()
