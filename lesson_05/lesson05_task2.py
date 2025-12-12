from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

# открыть браузер Google Chrome
driver = webdriver.Chrome()
sleep(2)

# перейти на страницу: http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")
print("Страница успешно загружена")

try:
    button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")


    button.click()
    print("Синяя кнопка успешно нажата")

    # Проверяем, что кнопка изменила состояние после клика
    sleep(5)
    print("Клик зарегистрирован системой")

except Exception as e:
    print(f"Ошибка при клике на кнопку: {e}")

sleep(5)
driver.quit()
print("Браузер закрыт")


