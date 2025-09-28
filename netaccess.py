#!path_to_python_bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#------------
# Inputs
#------------

userName = "type your user name"
password = "password"

#===========================
# Modify for slow net
#===========================

waiting_time = 0.1

#===============================================
# Automated part
#===============================================

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)
driver.get("https://netaccess.iitm.ac.in/login")

input_element = driver.find_element(By.ID, "username")
input_element.send_keys(userName)

input_element = driver.find_element(By.ID, "password")
#input_element.send_keys(password+ Keys.ENTER)
input_element.send_keys(password)#+ Keys.ENTER)

input_element = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
input_element.click()

time.sleep(waiting_time)

input_element = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary.btn-lg')
input_element.click()

time.sleep(waiting_time)

input_element = driver.find_element(By.ID, "self_duration")
select = Select(input_element)
select.select_by_value('2')

input_element = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
input_element.click()

time.sleep(waiting_time)

input_element = driver.find_element(By.ID, "btnAupAccept")
input_element.click()

driver.quit()