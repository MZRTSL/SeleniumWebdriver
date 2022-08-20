"""Select Datepicker fields (working with frame) - add a needed date"""
# Scenario 10. Lesson 32

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://jqueryui.com/")

date_picker = driver.find_element(By.LINK_TEXT, 'Datepicker')
date_picker.click()

# find frame html body/ if we don`t do it we can't find field click
calendar_field_frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(calendar_field_frame)
# driver.switch_to.frame(0) - find index

"Select a needed date"
field = driver.find_element(By.ID, 'datepicker')
field.send_keys('08/14/2022')

time.sleep(5)
driver.quit()
