"""Capture size, location and getAttribute 'class'  of drop and down"""
# Scenario 12. Lesson 35

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)

frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame)

# find drag
drag_me_target = driver.find_element(By.ID, 'draggable')

# find 'drop me' area
drop_me = driver.find_element(By.ID, 'droppable')

# Action - drop target to drop area
ActionChains(driver).drag_and_drop(drag_me_target, drop_me).perform()

time.sleep(2)
driver.quit()
