from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

# поиск поля и ввод значения
    driver.find_element(By.NAME, "custname").send_keys("Надежда")
# поиск кнопки и нажатие
    driver.find_element(By.XPATH, "//button[text()='Submit order']").click()
# проверка адреса
    driver_url = driver.current_url
    assert driver_url != "https://httpbin.org/forms/post"

    driver.quit()
