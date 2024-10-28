import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()

browser.get("https://www.saucedemo.com/")
browser.maximize_window()

#Login credentials

user = "standard_user"
password = "secret_sauce"

browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user)
browser.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
browser.find_element(By.XPATH, "//input[@id='login-button']").click()



#Click the button to order the prices from low to high
dropdown = Select(browser.find_element(By.XPATH, "//select[@class='product_sort_container']"))
dropdown.select_by_value("lohi")


#Extract all prices in a list.

price_elements = browser.find_elements(By.CLASS_NAME,"inventory_item_price")

#Convert prices to float

prices = [float(price.text.replace("$", "")) for price in price_elements]

#Asserting the prices are displayed from low to high, Assertion is done by comparing the results with the ordered list that we captured.
time.sleep(2)

assert prices == sorted(prices), "The prices are not ordered from lowest to highest"
print("The prices were ordered properly")

browser.quit()