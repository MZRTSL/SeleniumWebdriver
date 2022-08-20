"""ukrpravda test case 1 """

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.pravda.com.ua/")

burger_menu = driver.find_element(By.CLASS_NAME, "icon-menu")
burger_menu.click()

accept_button = driver.find_element(By.XPATH, '//div[2]/nav[2]/ul/li[9]/a')
accept_button.click()

orange_button = driver.find_element(By.XPATH, "//div[@id='general_frontpage']/div/div[2]/div/span/a/span")
orange_button.click()

search_field = driver.find_element(By.ID, 'pb-input')
search_field.click()
search_field.send_keys('Україна')

search_button = driver.find_element(By.ID, 'pb-submit')
search_button.click()

time.sleep(2)
driver.quit()
