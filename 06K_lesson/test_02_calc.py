from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_02_calc():
    # 1 Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2 В поле ввода по локатору #delay введите значение 45.
    delay_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#delay")
        ))
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
    result = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "screen")
    )).text
    print(result)
    #assert result.text == "15"
    driver.quit()
