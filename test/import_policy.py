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

driver.get("https://10.201.64.110/#dashboard")

#driver.implicitly_wait(10)

#ya_wait
wait = WebDriverWait(driver, 60, poll_frequency=1)
wait_user_name = ("xpath", "//input[@autocomplete='username']")
wait.until(EC.visibility_of_element_located(wait_user_name)).click()

#login
wait.until(EC.visibility_of_element_located(wait_user_name)).click()
driver.find_element("xpath", "//input[@autocomplete='username']").send_keys("superadmin")
driver.find_element("xpath", "//input[@type='password']").click()
driver.find_element("xpath", "//input[@type='password']").send_keys("Zaq1@wsX")
driver.find_element("xpath", "//div/button").click()

#home
wait_element = ("xpath", "//span/span/span")
wait.until(EC.visibility_of_element_located(wait_element))
#refresh_to_skip_red_window
driver.refresh()
#wait_refresh
wait.until(EC.visibility_of_element_located(wait_element))
#move_to_left_panel
element_to_hover_over = driver.find_element("xpath", "//span/span/span")
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
#open_policy
driver.find_element("xpath", "//span[@data-ref= 'btnInnerEl' and text()='Политика']").click()
#move_to_close_left_panel
click_empty = ("xpath", "//div/i[contains(@nztype, 'zone:warning-zone')]")
wait.until(EC.visibility_of_element_located(click_empty)).click()
#download_window
driver.find_element("xpath", "//i[@nztype='toolbar:download']").click()
time.sleep(3)
driver.find_element("xpath", "//span[.//text()=' Загрузить из файла ']").click()
time.sleep(3)
#download_new_policy
driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}/downloads/policy.xml")
#wait_to_click_import
button_import = ("xpath", "//div/button/span[@class='ng-star-inserted' and text()=' Импортировать политику ']")
wait.until(EC.element_to_be_clickable(button_import)).click()
#wait_window_accept_import
button_accept = ("xpath", "//button/span[text()=' Да, импортировать с перезаписью ']")
wait.until(EC.visibility_of_element_located(button_accept)).click()
#wait_black_window
black_window = ("xpath", "//div/label[text()='Импортирование прошло успешно']")
wait.until(EC.visibility_of_element_located(black_window))
print("Политика импортирована")
#proverka vod login
#test_login = driver.find_element("xpath", "//input[@autocomplete='username']").get_attribute("value")
#print(test_login)

#driver.find_element("id", "textfield-1013-inputEl").click()
#driver.find_element("id","textfield-1013-inputEl").clear()
#driver.find_element("id","textfield-1013-inputEl").send_keys("superadmin")
#driver.find_element("id","textfield-1017-inputEl").click()
#driver.find_element("id","textfield-1017-inputEl").clear()
#driver.find_element("id","textfield-1017-inputEl").send_keys("Zaq1@wsX")
#driver.find_element_by
#time.sleep(3)
#driver.find_element("xpath",u"//*/text()[normalize-space(.)='Войти']/parent::*").click()
#time.sleep(5)
