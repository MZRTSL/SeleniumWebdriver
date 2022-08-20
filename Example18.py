"""Handler drop and down"""
# Scenario 11. Lesson 33

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# or we can use import 'from selenium.webdriver.common.action_chains import ActionChains' it is equal
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")
time.sleep(3)

frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame)

obj = driver.find_element(By.ID, 'draggable')

# How we will see that actions is done? Using ActionChains.
# in ActionChains.drag and drop we have 2 options:
# drag_and_drop - if we know where we want to drop
# drag_and_drop_by_offset - select if we don`t know where we want to drop

ActionChains(driver).drag_and_drop_by_offset(obj, 150, 150).perform()
# 150 - it is size from border = x-crdnts and y-crdnts;
# 'perform()' - which used for perform that operation on the browser

time.sleep(3)
driver.quit()
