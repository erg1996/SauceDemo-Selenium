from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

browser.get("https://www.saucedemo.com/")
browser.maximize_window()

#Login credentials

user = "eduardo"
password = "pw123"

#Locate the user and password fields in the website

user_field = browser.find_element(By.XPATH, "//input[@id='user-name']")
password_field = browser.find_element(By.XPATH, "//input[@id='password']")
login_button = browser.find_element(By.XPATH, "//input[@id='login-button']")

#Filling out the login information

user_field.send_keys(user)
password_field.send_keys(password)
login_button.click()



error_message = browser.find_element(By.XPATH, "//h3[@data-test='error']")

try:
    assert error_message.is_displayed()
    print("The error message is displayed correctly")
except Exception as e:
    print("The test failed")
finally:
    browser.quit()
