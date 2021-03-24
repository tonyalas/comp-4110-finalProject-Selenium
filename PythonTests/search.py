#Selenium webdriver tests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Set the path variables
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Get the link to the website we're testing
driver.get("https://www.litcharts.com/")
#print(driver.title)

#Find the search element
search = driver.find_element_by_id("search-input")

#Enter the string 'ticket' to search for results
search.send_keys("George Orwell")

#Hit enter to preform the actual search
search.send_keys(Keys.RETURN)

titles = driver.find_elements_by_class_name("title")
for x in titles:
	print(x.text)

time.sleep(5)

#Exit the application
driver.quit()

