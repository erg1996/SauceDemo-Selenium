import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get("https://www.saucedemo.com/")
browser.maximize_window()

#Login credentials

user = "standard_user"
password = "secret_sauce"

browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user)
browser.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
browser.find_element(By.XPATH, "//input[@id='login-button']").click()

#Adding 2 products to the cart

product1 = browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
product2 = browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")

product1.click()
product2.click()

#going to the cart

browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

#clicking the checkout button

browser.find_element(By.XPATH, "//button[@id='checkout']").click()

#filling out the checkout form.

browser.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Eduardo")
browser.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Rivas")
browser.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("80223")
time.sleep(2)

#Sending the form

browser.find_element(By.XPATH, "//input[@id='continue']").click()
time.sleep(2)
browser.find_element(By.XPATH, "//button[@id='finish']").click()
time.sleep(2)
browser.quit()


