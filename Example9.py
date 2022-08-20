"""How to handle a dropdown"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65")

voice_search = driver.find_element(By.ID, 'rpp')
voice_search.send_keys('10')

time.sleep(2)
driver.quit()
