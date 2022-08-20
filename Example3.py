import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/Igor/PycharmProjects/SeleniumExamples/drivers/chromedriver')

driver.get("https://www.bing.com")

logo = driver.find_element(By.ID, "sb_form_q")
logo.click()
logo.send_keys("test")

icon = driver.find_element(By.XPATH, "//label[@for='sb_form_go']")
icon.click()

time.sleep(2)
driver.quit()
