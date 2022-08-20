"""FindElements - get text from dropdown"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://developer.salesforce.com/signup")

# p1=driver.find_elements_by_tag_name("option")
#
# driver.findElement: it will try to identify in the entire webpage
#     but as per our scenario we need to get data from the role dropdown
# so increase of using driver.fundElement ui can use find.findElement

obj = driver.find_element(By.CSS_SELECTOR, "dw-de-signup-form")

p1 = obj.find_elements(By.TAG_NAME, 'option')

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

time.sleep(2)
driver.quit()
