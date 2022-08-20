"""Select Datepicker fields (working with frame) - add a needed date MANUALLY"""
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

"Select a needed date MANUALLY"
field = driver.find_element(By.ID, 'datepicker')
field.click()

#  I observe what date starting with tag 'a'
# so we can use linkText command to perform click operation
# usually if anything is starting with tagname a if you want to perform click operation
# we can use linkText tag a commands

# but the date selected for current month
# if we need select next button date
# so we need select next month button '>' before select date

next_month_button = driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click
driver.find_element(By.LINK_TEXT, '31').click()

time.sleep(5)
driver.quit()
