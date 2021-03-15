import time
from selenium import webdriver

driver = webdriver.Safari()
driver.get('https://www.facebook.com');
time.sleep(5) # Let the user actually see something!
login_button = driver.find_element_by_name('email')
login_button.send_keys('tony_alas99@hotmail.com')
login_button = driver.find_element_by_name('pass')
login_button.send_keys('tonyalas99')
login_button.submit()
#driver.click(login_button)
time.sleep(10) # Let the user actually see something!
driver.quit()