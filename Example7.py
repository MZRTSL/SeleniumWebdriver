import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65")

check_box = driver.find_element(By.ID, 'vsread').is_selected()
print(check_box)

"is_selected() true or false : if is checked mode then it will return else it will return false"

if check_box:
    print("already checked") # if value is true = check box selected
else:
    driver.find_element(By.ID, 'vsread').click()
    print('successfully checked it')

time.sleep(2)
driver.quit()
