"""perform tab operation on all the links in the bing.com"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# below command maximized window browser
driver.maximize_window()
driver.get("https://www.bing.com")

p1 = driver.find_elements(By.TAG_NAME, "a")

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
        p1[element].send_keys(Keys.TAB)

time.sleep(5)
driver.quit()
