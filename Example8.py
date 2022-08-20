"""Handle a radio button"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65")

strict_radio_button = driver.find_element(By.ID, 'adlt_set_strict')
strict_radio_button.click()

# isSelected command to know the status of checkbox
# is True, if not selected radio button return False
strict_radio_button = driver.find_element(By.ID, 'adlt_set_strict').is_selected()
print(strict_radio_button)

time.sleep(2)
driver.quit()
