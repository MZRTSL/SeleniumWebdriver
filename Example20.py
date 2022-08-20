"""Perform resizeble operation"""
# Scenario 12. Lesson 35

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://jqueryui.com/resizable/")
time.sleep(3)

frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame)

obj = driver.find_element(By.XPATH, '//div[@class="ui-resizable-handle ui-resizable-se ui-icon '
                                    'ui-icon-gripsmall-diagonal-se"]')

ActionChains(driver).drag_and_drop_by_offset(obj, 150, 150).perform()
# 150 - it is size from border = x-crdnts and y-crdnts;
# 'perform()' - which used for perform that operation on the browser

time.sleep(3)
driver.quit()
