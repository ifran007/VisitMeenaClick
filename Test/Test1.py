from selenium import webdriver
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

driver = webdriver.Chrome("../drivers/chromedriver.exe")
# driver = webdriver.Chrome("C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
# driver = webdriver.Firefox("C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/drivers/geckodriver.exe")


driver.set_page_load_timeout("10")
driver.get("https://www.alibaba.com/").click()
time.sleep(10)
driver.quit()
