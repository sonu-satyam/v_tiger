from Library.lib import SeleniumWrapper
from Library.excel import read_locators

class DelOppor:
    locators = read_locators("deloppor")

    def __init__(self,driver):
        self.driver = driver

    def del_oppor(self):
        a = SeleniumWrapper(self.driver)
        a.click_element(DelOppor.locators["open_oppor"])
        a.click_element(DelOppor.locators["select_oppor"])
        a.click_element(DelOppor.locators["delete"])
        a.pop_up_accept()

