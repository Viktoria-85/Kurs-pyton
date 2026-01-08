from idlelib.format import FormatParagraph

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time




edge_driver_path = r"C:\Users\viktu\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))
driver.get("http:/bonigarcia.dev/selenium-webdriver-java/data-types.html")



def test_forma_elements():
     first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
     first_name.send_keys('Иван')
     first_name.click()


     last_name = driver.find_element(By.CSS_SELECTOR, "[name= last-name]")
     last_name.send_keys('Петров')
     last_name.click()


     address_input = driver.find_element(By.CSS_SELECTOR, "[name= address]")
     address_input.send_keys('Ленина,55-3')
     address_input.click()


     email_address = driver.find_element(By.CSS_SELECTOR, "[name= 'e-mail']")
     email_address.send_keys('test@skypro.com')
     email_address.click()

     phone_number = driver.find_element(By.CSS_SELECTOR, "[name= 'phone']")
     phone_number.send_keys('+7985899998787')
     phone_number.click()


     zip_code = driver.find_element(By.CSS_SELECTOR, "[name= 'zip-code']")
     zip_code.send_keys("")
     zip_code.click()


     city_name = driver.find_element(By.CSS_SELECTOR, "[name= 'city']")
     city_name.send_keys('Moсква')
     city_name.click()


     country_name = driver.find_element(By.CSS_SELECTOR, "[name= 'country']")
     country_name.send_keys('Россия')
     country_name.click()


     job_position = driver.find_element(By.CSS_SELECTOR, "[name= 'job-position']")
     job_position.send_keys('QA')
     job_position.click()


     company_name = driver.find_element(By.CSS_SELECTOR, "[name= 'company']")
     company_name.send_keys('SkyPro')
     company_name.click()

     button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
     button.click()


     elements = driver.find_elements(By.CSS_SELECTOR, "[name= 'zip-code']")
     for element in elements:
       assert '255, 0, 0' in element.value_of_css_property("background-color")


       elements = driver.find_elements(By.CSS_SELECTOR, "[name='first-name'], [name='last-name'], "
        "[name='address'], [name='e-mail'], [name='phone'], [name='city'], "
        "[name='country'], [name='job-position'], [name='company']")


       for element in elements:
          assert '0, 128, 0 ' in element.value_of_css_property("background-color")



       driver.quit()
























