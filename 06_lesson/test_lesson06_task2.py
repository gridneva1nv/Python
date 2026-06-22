from blib2to3.pgen2 import driver
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Откройте страницу https://gitflic.ru
    driver.get("https://gitflic.ru")

    # Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZGFhMDljOGMtMTc2Zi00ZWQxLTgxMDctNGVmZmViYmExNTUz",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/hoper")

    # Сохраните текущий URL.
    url_user1 = driver.current_url

    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()

    # Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "NDkwZDE5ZjYtNzI5Yy00NjFhLWJiNDYtNGUxNGZlOTAwOTNj",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/airsworld")

    # Сохраните текущий URL.
    url_user2 = driver.current_url

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2

    driver.delete_all_cookies()
    driver.quit()
