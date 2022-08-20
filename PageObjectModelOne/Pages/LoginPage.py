from selenium.webdriver.common.by import By


class LoginPageProp():

    def __init__(self, driver):
        self.driver = driver

    user_name_xpath = "//input[@name='uname']"
    password_xpath = "//input[@name='pass']"
    login_button_xpath = "//input[@value='login']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.user_name_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def press_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()


# self.driver.find_element(By.XPATH, loginProp.password_xpath).send_keys("test")
        # self.driver.find_element(By.XPATH, loginProp.login_button_xpath).click()
