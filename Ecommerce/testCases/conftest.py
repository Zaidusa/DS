# import pytest
# from selenium import webdriver
#
# # @pytest.fixture()
# # def setup(self):
# #     driver = webdriver.Chrome()
# #     driver.implicitly_wait(60)
# #     driver.maximize_window()
# #     return driver
#
# @pytest.fixture()
# def setup(browser):
#     if (browser=="chrome"):
#         driver = webdriver.Chrome()
#         return driver
#     else:
#         driver = webdriver.Chrome()
#         return driver
#
#
# def pytest_addoption(parser):
#      parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")