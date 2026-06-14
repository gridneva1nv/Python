from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

# поиск ссылок
    links = driver.find_elements(By.XPATH, "//a")
# проверка количества ссылок
    assert len(links) == 10
# проверка видимости ссылок
    for link in links:
        assert link.is_displayed()
# проверка содержимого 1й ссылки
    assert links[0].text == "1"

    driver.quit()
