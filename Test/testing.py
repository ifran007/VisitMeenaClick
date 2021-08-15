from selenium import webdriver
import unittest
import time
import HtmlTestRunner

class MeenaBazar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_visit_meenaBazar(self):
        self.driver.get("https://www.meenaclick.com/")
        self.driver.find_element_by_xpath("//div[@class='hidden-pc top-fixed']//li[3]//a[1]//button[1]").click()

    # def test_visit_meenaBazar(self):
    #     self.driver.get("https://www.meenaclick.com/")
    #     self.driver.find_element_by_xpath("//header[@class='header']//img[@alt='Logo']").click()

    # def test_visit_meenaBazar(self):
    #     self.driver.get("https://www.meenaclick.com/")
    #     self.driver.find_element_by_css_selector("header[class='header'] img[alt='Logo']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        time.sleep(20)
        print("Test concluded")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/Reports'))