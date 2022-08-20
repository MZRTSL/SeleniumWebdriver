"""How to handle a dropdown=dd"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65")

voice_search_dd = driver.find_element(By.ID, 'rpp')

# add means it is a dropdown information itself
# if you want to select first value in the dd then we need to get index as 0
# if we want to select 2nd value from dd we need to gen index 1

s = Select(voice_search_dd)
# s.select_by_index(2) - using this command for selecting using position number
# s.select_by_value('30')
# s.select_by_visible_text('Авто')

p1 =s.options
# print(p1)

# options: which will be capture all the values in the dropdown, and it will store in the variable/
# when we use print stmt
# it is printing all the web element, but we need text values in dd from all the object

for element in p1:
    p2=element.get_attribute('value')
    print(p2)

time.sleep(5)
driver.quit()
