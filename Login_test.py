from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

browser.get("https://www.saucedemo.com/")
browser.maximize_window()

#Login credentials

user = "standard_user"
password = "secret_sauce"

#Locate the user and password fields in the website

user_field = browser.find_element(By.XPATH, "//input[@id='user-name']")
password_field = browser.find_element(By.XPATH, "//input[@id='password']")
login_button = browser.find_element(By.XPATH, "//input[@id='login-button']")

#Filling out the login information

user_field.send_keys(user)
password_field.send_keys(password)
login_button.click()

#Once we're in, assert the text "Products" is present in the inventory page.

page_text = browser.find_element(By.XPATH, "//span[@class='title']")

try:
    assert page_text.text == "Products", "Login was not succesful"

    print("Login was succesful")
finally:
    browser.quit()

