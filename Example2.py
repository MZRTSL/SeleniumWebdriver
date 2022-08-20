import time

from selenium import webdriver

# drivers/chromedriver - it is address in project 'SeleniumExample' all drivers
# in field - '/Пользователи/Igor/PycharmProjects/SeleniumExamples/' - will update
driver = webdriver.Chrome('drivers/chromedriver')
driver.get('http://selenium.dev/')

time.sleep(2)
driver.quit()
