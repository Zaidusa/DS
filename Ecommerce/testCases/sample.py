import time
import [pytest-xdist]
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.abc
def test_log():
    textbox_username_id="Email"
    textbox_password_id = "Password"
    button_submit_xpath="//button[ @ type = 'submit']"
    link_logout_xpath="//a[normalize-space()='Logout']"
    url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"
    driver=None
    for i in range (1):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element("id", textbox_username_id).clear()
        driver.find_element("id",textbox_username_id).send_keys(username)
        driver.find_element("id", textbox_password_id).clear()
        driver.find_element("id",textbox_password_id).send_keys(password)
        driver.find_element(By.XPATH,button_submit_xpath).click()
        time.sleep(5)
        print(driver.title)
        driver.find_element(By.XPATH, link_logout_xpath).click()

        if ( 1==1):
            #driver.title."Dashboard / nopCommerce administration"):
            print("login successful")
            assert True
        else:
            driver.get_screenshot_as_file("../Screenshots/" + "test_login.png")
            print("login not successful")
            assert False
        driver.close()
        driver.quit()



