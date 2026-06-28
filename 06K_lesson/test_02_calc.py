from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_02_calc():
    # 1 Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 45)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2 В поле ввода по локатору #delay введите значение 45.
    delay_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#delay")
        ))
    delay_field.clear()
    delay_field.send_keys("45")

    # 3 Нажмите на кнопки: 7 + 8 =
    keys = ["7", "+", "8", "="]
    for key in keys:
        print(f"//span[text() = '{key}']")
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[text() = '{key}']")
            ))
        button.click()

    # 4 Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    start = time.perf_counter()
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, ".screen").text.strip() == "15")
    timer = time.perf_counter() - start
    result = driver.find_element(By.CLASS_NAME, "screen").text.strip()

    print(result, timer)
    assert int(timer) == 45
    driver.quit()
