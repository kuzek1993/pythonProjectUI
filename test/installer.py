import time

import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
#options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://10.201.67.195:8081/")
time.sleep(3)

INSTALL_RADIO=("xpath", "//label[@data-testid='mode,install']")
UPDATE_RADIO=("xpath", "//label[@data-testid='mode,update']")
MODIFY_RADIO=("xpath", "//label[@data-testid='mode,modify']")

driver.find_element(*UPDATE_RADIO).click()
time.sleep(3)
driver.find_element("xpath", "//button[@data-testid='next_step_button']").click()
time.sleep(3)