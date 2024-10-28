import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get("https://www.saucedemo.com/")
browser.maximize_window()

#Login credentials

user = "standard_user"
password = "secret_sauce"

user_field = browser.find_element(By.XPATH, "//input[@id='user-name']")
password_field = browser.find_element(By.XPATH, "//input[@id='password']")
login_button = browser.find_element(By.XPATH, "//input[@id='login-button']")


# login to the page

user_field.send_keys(user)
password_field.send_keys(password)
login_button.click()

time.sleep(2)

# Get the product´s name and price and then Locate the Add to cart button of a product
product_name = browser.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']").text
product_price = browser.find_element(By.XPATH, "//div[3]//div[2]//div[2]//div[1]").text
addToCart = browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
time.sleep(2)


#Adding the item to the cart

addToCart.click()

time.sleep(2)

cart_button = browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_items = browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")

time.sleep(5)

cart_button.click()


#Confirm the item we selected was added to the cart, validate name and price.

nameProductInCart = browser.find_element(By.XPATH, "//div[@class='inventory_item_name']")
priceProductInCart = browser.find_element(By.XPATH, "//div[@class='inventory_item_price']")

try:
    assert nameProductInCart.text == product_name, "The product's name is not correct"
    assert priceProductInCart.text == product_price, "The product's price is not correct"
    print("The name and price of the product are correct")
finally:
    browser.quit()


