"""Handle a ALERT"""
# # Scenario 21. Lesson 44

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.support import expected_conditions as EX

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

# 1 ALERT
# click on button for shown alert
driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()

a = driver.switch_to.alert
print(a.text)
a.accept()
print('successfully handle 1 alert')

# 2 ALERT
# find alert option wit OK option and alert text
driver.find_element(By.XPATH, "//a[contains(text(),'Alert with OK & Cancel')]").click()

# click on button for shown alert
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

a = driver.switch_to.alert
print(a.text)
a.accept()
print('successfully handle 2 alert')

# 3 Alert
# find alert option wit OK option and alert text
driver.find_element(By.XPATH, "//a[contains(text(),'Alert with Textbox ')]").click()

# click on button for shown alert
driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

a = driver.switch_to.alert
print(a.text)
a.accept()
print('successfully handle 3 alert')

time.sleep(3)
driver.quit()
