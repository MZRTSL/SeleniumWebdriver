"""Capture message from tooltips"""
# Scenario 14. Lesson 36

import time
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://jqueryui.com/tooltip/")
time.sleep(3)

frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame)

# find field with tooltips message
field = driver.find_element(By.ID, 'age')
# find where tooltips message text located for this field
# use getAttribute command for that object ( and use title input, directly print that message to the console
p1 = field.get_attribute('title')
print('Tooltip message is: ' + p1)

time.sleep(2)
driver.quit()
