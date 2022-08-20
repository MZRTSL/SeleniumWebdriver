"""Handle mouse over"""
# Scenario 16. Lesson 38

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.emirates.com/ca/english/")
driver.maximize_window()

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

# click on point
under_point3 = driver.find_element(By.XPATH, "//i[contains(.,'At the airport')]")
under_point3.click()

time.sleep(3)
driver.quit()
