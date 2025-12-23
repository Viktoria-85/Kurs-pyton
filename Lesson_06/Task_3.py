# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 20)
driver.maximize_window()
# дождаться, когда картинки загрузятся
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

#найти 3 картинку
third_image = driver.find_element(By.CSS_SELECTOR, "#image-container img:nth-child(3)")

# получить значение атрибута src
third_image_src = third_image.get_attribute("src")
print(f"Атрибут src 3-й картинки: {third_image_src}")

driver.quit()






















