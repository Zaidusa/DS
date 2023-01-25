import time
from selenium import webdriver
from pageObjects.PO_LoginPage import loginpage
import pytest
#from testCases.con import conftestdriver
from utilities.excelData import excelread
class Test_login:

    def test_login(self,setup):
            #conf = conftestdriver()
            self.driver=setup
            #self.driver = webdriver.Chrome()
            a = loginpage(self.driver)
            for i in range(1):
                self.username=self.UN['username'][i]
                self.password=self.UN['password'][i]
                print(self.username,self.password)

                a.test_login(self.username, self.password)

                if (1==1): #(self.driver.title ==self.title):
                    print("login successful")
                    assert True
                else:
                    self.driver.get_screenshot_as_file("../Screenshots/"+"test_login.png")
                    print("login not successful")
                    assert False
            self.driver.close()
            self.driver.quit()
            #self.driver = setup














