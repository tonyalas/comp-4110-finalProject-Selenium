#Selenium webdriver tests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#gets all the hits
hits = driver.find_elements_by_class_name("hit-item")

#reads through hits
for hit in hits:

	#gets title in hits
	title = hit.find_element_by_class_name("title")

	#This whole block makes sure it's not printing the blurred text
	tester = title.get_attribute('class')
	check = False
	if tester == 'title blurred-text':
		continue
	else:
		print(title.text)


time.sleep(5)

#Exit the application
driver.quit()

