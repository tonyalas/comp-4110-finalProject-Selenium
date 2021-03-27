#Selenium webdriver tests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Set the path variables
PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Get the link to the website we're testing
driver.get("https://www.litcharts.com/")
#print(driver.title)

#Find the loginButton element
link = driver.find_element_by_link_text("Sign In")
link.click()

#get the username input field
user = driver.find_element_by_id("user[signin]")

#Enter the string 'ticket' to search for results
user.send_keys("SeleniumTester99")

#Now the password
mypass = driver.find_element_by_id("user[password]")
mypass.send_keys("SeleniumTests")

#Hit enter to login
mypass.send_keys(Keys.RETURN)

time.sleep(5)

#Exit the application
driver.quit()

