from Library.lib import SeleniumWrapper
from Library.excel import read_locators

class AddLead:
    locators = read_locators("addleads")
    # print(locators)
    def __init__(self,driver):
        self.driver = driver

    def create_lead(self,salutation,fname,lname,company,designation,lead_source):
        a = SeleniumWrapper(self.driver)
        a.click_element(AddLead.locators["openlead"])
        a.click_element(AddLead.locators["add_lead"])
        a.dropdwon(AddLead.locators["salutation"],salutation)
        a.send_data(AddLead.locators["fname"],fname)
        a.send_data(AddLead.locators["lname"],lname)
        a.send_data(AddLead.locators["company"],company)
        a.send_data(AddLead.locators["designation"],designation)
        a.dropdwon(AddLead.locators["lead_source"],lead_source)
        a.click_element(AddLead.locators["save"])