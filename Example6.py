import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65")

check_box = driver.find_element(By.ID, 'vsread')
check_box.click()

'''click is a command will toggle the status of the checkbox
but my require nt is i dont want to toggle it.. based on the status of checked i need o update it

if my checkbox is in checked mode: then simply print a message that is already checked
if it is not checked mode then check it and print a message that successfully'''

time.sleep(2)
driver.quit()
