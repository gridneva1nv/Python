from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_03_shop():
    # 1 Откройте сайт магазина: https://www.saucedemo.com/ в FireFox
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # 2 Авторизуйтесь как пользователь standard_user
    wait.until(EC.presence_of_element_located(
        (By.ID, "user-name")
    )).send_keys("standard_user")

    wait.until(EC.presence_of_element_located(
        (By.ID, "password")
    )).send_keys("secret_sauce")

    button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    button.click()

    # 3 Добавьте в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T-Shirt.
    # Sauce Labs Onesie.
    products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]
    for product in products:
        add_button = f"add-to-cart-{product}"
        # print(add_button)
        button = driver.find_element(By.ID, add_button)
        button.click()

    # 4 Перейдите в корзину
    button = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link")
    ))
    button.click()

    # 5 Нажмите Checkout
    button = wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout")
    ))
    button.click()

    # 6 Заполните форму своими данными:
    # имя,
    # фамилия,
    # почтовый индекс
    fields = {
        "first-name": "Надежда",
        "last-name": "Гриднева",
        "postal-code": "346398"
    }
    for name, value in fields.items():
        field = wait.until(EC.presence_of_element_located(
            (By.ID, name)
        ))
        field.send_keys(value)

    # 7 Нажмите кнопку Continue
    button = wait.until(EC.element_to_be_clickable(
        (By.ID, "continue")
    ))
    button.click()

    # 8 Прочитайте со страницы итоговую стоимость (Total)
    total = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "summary_total_label")
    )).text
    # print(total)

    # 9 Закройте браузер
    driver.quit()

    # 10 Проверьте, что итоговая сумма равна $58.29
    assert total == "Total: $58.29"
