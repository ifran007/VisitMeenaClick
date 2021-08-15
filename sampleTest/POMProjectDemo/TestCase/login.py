from selenium import webdriver
import unittest
import time
import HtmlTestRunner

class MeenaBazar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Search(self):
        self.driver.get("https://www.meenaclick.com/")
        self.driver.find_element_by_xpath("//app-root//input[@type='text']").send_keys("dry")

    def test_Area(self):
        self.driver.get("https://www.meenaclick.com/")
        # self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-header/div[1]/div[1]/div/div/header/div[3]/a[1]/div[2]/div[1]").click()
        self.driver.find_element_by_xpath("//header//div[3]//a[1]").click()

    def test_Signin_Register(self):
        self.driver.get("https://www.meenaclick.com/")
        self.driver.find_element_by_xpath("//header/div[3]/a[2]/div[2]/div").click()
        self.driver.find_element_by_xpath("/html/body/app-root/layout-passport/nz-layout/div/passport-login/div/div/div/div/div[2]/form/nz-form-item[3]/nz-form-control/div/div/button[2]").click()

    def test_Categories(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-header/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div").click()

    def test_NoItem(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath('/html/body/app-root/layout-default/nz-layout/app-header/div[1]/div[1]/div/div/header/div[3]/a[3]/div[2]').click()

    def test_Recipe(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[@routerlink='/recipe']//button[@type='button']").click()

    def test_TrackOrder(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//ul[@class='list-nav float-right']//li[2]//a[1]//button[1]").click()

    def test_Combo(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-header/div[1]/div[2]/div/div/div/div/div[2]/ul[1]/li[1]/a/button").click()
        self.driver.find_element_by_xpath("// ul[ @class ='list-nav float-left pl-sm'] // li[1] // a[1] // button[1]").click()

    def test_Offers(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-header/div[1]/div[2]/div/div/div/div/div[2]/ul[1]/li[2]/a/button").click()
        # self.driver.find_element_by_xpath("//ul[@class='list-nav float-left pl-sm']//li[2]//a[1]//button[1]").click()

    def test_FlashSeals(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-header/div[1]/div[2]/div/div/div/div/div[2]/ul[1]/li[3]/a/button").click()
        # self.driver.find_element_by_xpath("//ul[@class='list-nav float-left pl-sm']//li[3]//a[1]//button[1]").click()

    def test_MeenaClickStores(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[normalize-space()='MeenaClick Stores']").click()

    def test_FrequentlyAskedQuestions(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-footer/div[1]/div[1]/div/div/div[1]/div/ul/li[2]/a").click()
        self.driver.find_element_by_xpath("//a[normalize-space()='Frequently Asked Questions']").click()

    def test_TermsConditions(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-footer/div[1]/div[1]/div/div/div[1]/div/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("//a[normalize-space()='Terms and Conditions']").click()

    def test_Coupons(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_link_text("Coupons").click()

    def test_PrivacyPolicy(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/app-footer/div[1]/div[1]/div/div/div[1]/div/ul/li[5]/a").click()
        # self.driver.find_element_by_xpath("//a[normalize-space()='Privacy Policy']").click()
        self.driver.find_element_by_link_text("Privacy Policy").click()

    def test_AboutMeenaClick(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[normalize-space()='About MeenaClick']").click()
        # self.driver.find_element_by_link_text("About MeenaClick").click()

    def test_ShippingDelivery(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("//a[normalize-space()='Shipping and Delivery']").click()
        self.driver.find_element_by_link_text("Shipping and Delivery").click()

    def test_CustomerCare(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("//a[normalize-space()='Customer Care']").click()
        self.driver.find_element_by_link_text("Customer Care").click()

    def test_Careers(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("//a[normalize-space()='Careers']").click()
        self.driver.find_element_by_link_text("Careers").click()

    def test_Facebook(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[@title='Facebook']//div[@class='icon-container']").click()

    def test_Instagram(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[@title='Instagram']//fa-icon[@class='ng-fa-icon icon']//*[local-name()='svg']").click()

    def test_Linkedin(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[@title='Linkedin']//div[@class='icon-container']").click()

    def test_Youtube(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[@title='Youtube']//div[@class='icon-container']").click()

    def test_FeaturedBrands(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//a[@href='/organikare']//img[@alt='Product Thumb']").click()

    def test_BabyCare(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Baby Care')]").click()

    def test_BakerySnacks(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@routerlink='/category/bakery-snacks']").click()

    def test_BeautyHygiene(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@routerlink='/category/beauty-hygiene']").click()

    def test_Beverages(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Beverages')]").click()

    def test_Dairy(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Dairy')]").click()
        # self.driver.find_element_by_xpath("/html/body/app-root/layout-default/nz-layout/div/app-home-default/div/div/div[1]/div[1]/div/div/ul/li[7]/span/span").click()

    def test_Fish(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Fish')]").click()

    def test_FreshProduce(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Fresh Produce')]").click()

    def test_Grocery(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Grocery')]").click()

    def test_HouseholdCleaning(self):
        self.driver.get("https://www.meenaclick.com")
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Household & Cleaning')]").click()

    def test_Meat(self):
        self.driver.get("https://www.meenaclick.com")
        # self.driver.find_element_by_xpath("/html[1]/body[1]/app-root[1]/layout-default[1]/nz-layout[1]/div[1]/app-home-default[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[12]/span[1]/span[1]").click()
        self.driver.find_element_by_xpath("//li[@class='ant-menu-item']//span//span[contains(text(),'Meat')]").click()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        time.sleep(10)
        print("Test concluded")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/Reports'))