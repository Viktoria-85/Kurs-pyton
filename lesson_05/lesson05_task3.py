from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# открыть браузер FireFox.
geckodriver = webdriver.Firefox()
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
geckodriver.get("http://the-internet.herokuapp.com/inputs")
print("страница успешно загружена")
sleep(5)

# Ввести в поле текст Sky.
input_field = geckodriver.find_element(By.TAG_NAME, "input")

input_field.send_keys("Sky")
print("Введен текст 'Sky'")
sleep(3)

# Очистить это поле (метод clear())
input_field.clear()
print("Поле очищено")
sleep(3)
# Ввести в поле текст Pro.
input_field.send_keys("Pro")
print("Введен текст 'Pro'")
sleep(3)
# Закрыть браузер (метод quit())
geckodriver.quit()
print("Браузер закрыт")

