import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from PageObjectModelOne.Pages.LoginPage import LoginPageProp
# from PageObjectModelOne.Pages.UserPage import UserInfo


# will write logic the lounch that browser n open the application when I will maximaze browser also
from PageObjectModelOne.Pages.UserPage import UserInfo


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://testphp.vulnweb.com/login.php")
        cls.driver.maximize_window()

    def test_a_login(self):
        driver = self.driver
        login = LoginPageProp(driver)
        login.enter_username("test")
        # self.driver.find_element(By.XPATH, loginProp.user_name_xpath).send_keys("test")
        login.enter_password("test")
        # self.driver.find_element(By.XPATH, loginProp.password_xpath).send_keys("test")
        login.press_login_button()
        # self.driver.find_element(By.XPATH, loginProp.login_button_xpath).click()
        time.sleep(3)

    def test_b_change_phoneNumber(self):
        driver=self.driver
        userPage = UserInfo(driver)
        userPage.enter_phone("12344")
        # self.driver.find_element(By.XPATH, userPage.phone_field_xpath).send_keys("12344")
        time.sleep(3)
        userPage.click_update()
        # self.driver.find_element(By.XPATH, userPage.update_button_xpath).click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/Igor/PycharmProjects/SeleniumExamples/report'),
        verbosity=2)
