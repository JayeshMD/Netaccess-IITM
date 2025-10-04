#!~/Netaccess-IITM/venv_netaccess/bin/python3
import os
import time
import getpass
import pickle as pkl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

#------------
# Inputs
#------------

try: 
    # Try to load data.
    with open(".conf/data.pkl", "rb") as f:
        data = pkl.load(f)
    
    username = data["username"]
    password = data["password"]

except:
    # If data is not avilable.
    username = input("username:")
    password = getpass.getpass("password:")
    try:
        os.mkdir(".conf")
    except:
        pass
    data = {"username": username, "password": password}
    with open(".conf/data.pkl", "wb") as f:
        pkl.dump(data, f)
    print("Data saved locally.")

#===========================
# Modify for slow net
#===========================

waiting_time = 0.1

#===============================================
# Automated part
#===============================================
service = Service(executable_path="")
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://netaccess.iitm.ac.in/login")

input_element = driver.find_element(By.ID, "username")
input_element.send_keys(username)

input_element = driver.find_element(By.ID, "password")
input_element.send_keys(password)

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