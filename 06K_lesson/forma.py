from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service = EdgeService(EdgeChromiumDriverManager().install())
browser = webdriver.Edge(service=service)
browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

browser.quit()
