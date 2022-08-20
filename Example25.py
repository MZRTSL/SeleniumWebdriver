"""Handle mouse over"""
# # Scenario 17. Lesson 39
# '''HOW WORKING WITH XPATH WITH MULTIVALUES'''

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.emirates.com/ca/english/")
driver.maximize_window()

# test which I need from the list of values
text2 = 'At the airport'

# Accept cookies
cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
cookies.click()

experience_button = driver.find_element(By.XPATH, "//a[contains(text(),'EXPERIENCE')]")
experience_button.click()

point1 = driver.find_element(By.LINK_TEXT, 'The Emirates Experience')
# moveElements it is command witch move cursor to object
ActionChains(driver).move_to_element(point1).perform()

point2 = driver.find_element(By.LINK_TEXT, 'Dubai Experience')
ActionChains(driver).move_to_element(point2).perform()

point3 = driver.find_element(By.LINK_TEXT, 'Family travel')
ActionChains(driver).move_to_element(point3).perform()

time.sleep(3)
# select under point, it is 99 values (list of values)
val = driver.find_elements(By.XPATH, "//i[@class='thirdlevel__menu-link']")

# finding needed value in 99 point list
for element in range(len(val)):

    text1 = val[element].text
    if text1 == text2:
        print(text1)
        val[element].click()
        break

print('Test completed')

time.sleep(3)
driver.quit()
