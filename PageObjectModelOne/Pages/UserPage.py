from selenium.webdriver.common.by import By


class UserInfo():

    def __init__(self, driver):
        self.driver = driver

    phone_field_xpath = "//input[@name='uphone']"
    update_button_xpath = "//input[@name='update']"

    def enter_phone(self, number):
        self.driver.find_element(By.XPATH, self.phone_field_xpath).send_keys(number)

    def click_update(self):
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()
