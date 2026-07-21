from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.amazon.in")

time.sleep(3)

print("Amazon page opened")
print("Page title:", driver.title)

search_box = driver.find_element(By.NAME, "field-keywords")
search_box.send_keys("wireless mouse")

search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

print("Product search completed")

time.sleep(8)

product_cards = driver.find_elements(
    By.XPATH,
    "//div[@data-component-type='s-search-result']"
)

print("Number of product cards found:", len(product_cards))
print()

product_number = 0

for card in product_cards:
    name_elements = card.find_elements(By.XPATH, ".//h2//span")
    price_elements = card.find_elements(By.CLASS_NAME, "a-price-whole")

    if len(name_elements) > 0:
        product_number = product_number + 1

        print("Product", product_number)
        print("Name:", name_elements[0].text)

        if len(price_elements) > 0:
            print("Price: Rs.", price_elements[0].text)
        else:
            print("Price: Not available")

        print()

    if product_number == 5:
        break

deals_link = driver.find_element(By.LINK_TEXT, "Today's Deals")

print("Link found using LINK_TEXT:", deals_link.text)

deals_link.click()

time.sleep(4)

print("Today's Deals page opened")
print("Current URL:", driver.current_url)

driver.quit()

print("Browser closed")
