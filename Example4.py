import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.bing.com")

logo = driver.find_element(By.ID, "sb_form_q")
logo.click()
logo.send_keys("test")

icon = driver.find_element(By.XPATH, "//label[@for='sb_form_go']")
icon.click()

time.sleep(2)
driver.quit()
