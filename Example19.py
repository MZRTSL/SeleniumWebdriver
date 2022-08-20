"""Capture size, location and getAttribute 'class'  of drop and down"""
# Scenario 13. Lesson 34

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")
time.sleep(3)

frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame)

obj = driver.find_element(By.ID, 'draggable')
# capture 'height' and 'width'
s=obj.size
# capture x ans y coordinates
l=obj.location

# show info above in console
print(s)
print(l)

# capture and print attribute for obj
print(obj.get_attribute('class'))