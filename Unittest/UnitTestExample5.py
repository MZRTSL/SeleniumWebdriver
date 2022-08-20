import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

"""ДОДЕЛАТЬ - урок 49 / part3"""


# will write logic the lounch that browser n open the application when I will maximaze browser also
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://testphp.vulnweb.com/login.php")
        cls.driver.maximize_window()

    def test_a_login(self):
        self.driver.find_element(By.XPATH, "//input[@name='uname']").send_keys("test")
        self.driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("test")
        self.driver.find_element(By.XPATH, "//input[@value='login']").click()
        time.sleep(15)

    def test_b_change_phoneNumber(self):
        self.driver.find_element(By.XPATH, "//input[@name='uphone']").send_keys("12344")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='update']").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/Igor/PycharmProjects/SeleniumExamples/report'),
        verbosity=2)
