from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

# переход на сайт
    driver.get("https://httpbin.org/")
# переход по ссылке
    driver.find_element(By.LINK_TEXT, "HTML form").click()
# проверка адреса
    driver_url = driver.current_url
    assert driver_url == "https://httpbin.org/forms/post"
# возврат на главную страницу
    driver.back()
# проверка адреса
    driver_url = driver.current_url
    assert driver_url == "https://httpbin.org/"

    driver.quit()
