from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# открыть браузер Chrome
driver = webdriver.Chrome()
sleep(5)

# перейти на страницу http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")
print("Страница успешно загружена")

# кликнуть на синюю кнопку Button
try:

    button = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        )
    )

    button.click()
    print("Синяя кнопка успешно нажата")

    # Обрабатываем всплывающее окно (alert)
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print("Alert успешно закрыт")

except Exception as e:
    print(f"Произошла ошибка: {e}")

sleep(10)
driver.quit()
print("Браузер закрыт")



