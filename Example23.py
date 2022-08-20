"""FindElements - find history text in browser, capture it and refund to console """
# Scenario 15. Lesson 37

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com")
driver.maximize_window()

# click on field for open history
driver.find_element(By.ID, 'sb_form_q').send_keys('tesla')
time.sleep(5)

p1 = driver.find_elements(By.XPATH, "//li[@class='sa_sg']")

# lend(list): total number of values in the list
print(len(p1))

# next cmnd shown the values in p1
for element in range(len(p1)):
    print(p1[element].text)

# capture screenshot and select address where it will be saved
driver.get_screenshot_as_file('/Users/Igor/Desktop/Разное/Python/Screenshots/demo2.png')
# 'demo22.png' - it is name pf new PNG that you add manually

time.sleep(5)
driver.quit()
