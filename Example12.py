"""FindElements - get text from all the links"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com/account/general?")

p1 = driver.find_elements(By.TAG_NAME, "option")
print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

time.sleep(2)
driver.quit()
