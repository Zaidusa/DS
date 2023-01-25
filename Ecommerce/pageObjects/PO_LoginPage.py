from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# what does an page objects needed.
#1. first create a class and under class create a constructor to invoke a driver when Testcase is called
#usually we maintain object identification variables in PO class

class loginpage:

    textbox_username_id="Email"
    textbox_password_id = "Password"
    button_submit_xpath="//button[ @ type = 'submit']"
    link_logout_xpath="//a[normalize-space()='Logout']"
    url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"


    def __init__(self,driver):
        self.driver=driver

    def test_login(self,username,password):
        self.driver.get(self.url)
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id",self.textbox_username_id).send_keys(username)
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()













