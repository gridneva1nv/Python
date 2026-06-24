from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#start button")
        # (By.XPATH, "//button[text() = 'Start']")
    ))
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    post = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#finish")
        # (By.XPATH, "//h4[text() = 'Hello World!']")
    ))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot('dynamic_loading.png')

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert post.text == "Hello World!"

    driver.quit()
