from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.google.com")

print("Google page opened")
print("Page title:", driver.title)

time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium tutorial")
search_box.send_keys(Keys.ENTER)

print("Search completed")

time.sleep(3)

print("Search page title:", driver.title)
print("Current URL:", driver.current_url)

driver.refresh()
print("Page refreshed")

time.sleep(2)

driver.quit()
print("Browser closed")
