from Library.lib import SeleniumWrapper
from Library.excel import read_locators

class Login:
    locators = read_locators("login")
    # print(locators)
    def __init__(self,driver):
        self.driver = driver

    def login(self):

        a = SeleniumWrapper(self.driver)
        a.send_data(Login.locators["username"],"admin")
        a.send_data(Login.locators["password"],"admin")
        a.click_element(Login.locators["click"])
