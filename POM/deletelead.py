from Library.lib import SeleniumWrapper
from Library.excel import read_locators

class DeleteLeads:
    locators= read_locators("delleads")
    # print(locators)

    def __init__(self,driver):
        self.driver = driver

    def dellead(self):
        a= SeleniumWrapper(self.driver)
        a.click_element(DeleteLeads.locators["openlead"])
        a.click_element(DeleteLeads.locators["edit"])
        a.pop_up_accept()
