from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# открыть браузер FireFox.
geckodriver = webdriver.Firefox()
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
geckodriver.get("http://the-internet.herokuapp.com/login")
print("страница успешно загружена")
sleep(5)

# В поле username ввести значение tomsmith
username_field = geckodriver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
print( "введено успешно: оtomsmith")

# В поле password ввести значение SuperSecretPassword!
password_field = geckodriver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
print( "введено успешно: SuperSecretPassword!")

# Нажать кнопку Login
login_button = geckodriver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
print("кнопка нажата успешно")

# Вывести текст с зеленой плашки в консоль
try:
   wait = WebDriverWait(geckodriver, 10)
   flash_message = wait.until(EC. presence_of_element_located((By.ID, "flash")))
   sleep(3)
#извлекаем текст из плашки
   flash_text = flash_message.text
   print(f"Текст плашки: {flash_text}")

except Exception as e:
       print(f"Ошибка при получении текста плашки: {e}")

# Закрыть браузер (метод quit())
geckodriver.quit()
print("Браузер закрыт")

