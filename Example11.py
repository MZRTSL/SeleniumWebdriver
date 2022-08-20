"""FindElements - get text from all the links"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com")

# we are using FindElement the output will be collection of
# multiple objects so we can use 'for loop' to print the value

p1 = driver.find_elements(By.TAG_NAME, "a")

# next cmnd shown the values with tag name a
for element in range(len(p1)):
    print(p1[element].text)

# lend(list): total number of values in the list
print(len(p1))

time.sleep(5)
driver.quit()
