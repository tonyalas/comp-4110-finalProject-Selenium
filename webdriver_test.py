import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    driver.get("https://www.litcharts.com/")
    driver.find_element(By.NAME, "query").send_keys("george orwell" + Keys.RETURN)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "1984")))
    driver.find_element_by_link_text("1984").click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a:nth-child(2) .naked")))
    driver.find_element_by_css_selector("a:nth-child(2) .naked").click()
    time.sleep(10)
    driver.quit()

