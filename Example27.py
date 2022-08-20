"""Handle a webtable - for table description columns"""
# # Scenario 19. Lesson 42

import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EX

# WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
WebDriverWait(driver, 10).until(EX.alert_is_present())

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/tags/default.asp")
driver.maximize_window()

beforeNumber = "//tr["
afterNumber = "]/td[2]"
# beforeNumber +2,3,4(nees to come from for loop) + afterNumber

for _ in range(2, 5):
    xp1 = beforeNumber + str(_) + afterNumber
    # p1=//tr[2]/td[1]
    value = driver.find_element(By.XPATH, xp1).text
    print(value)

time.sleep(3)
driver.quit()
