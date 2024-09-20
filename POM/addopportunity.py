from Library.lib import SeleniumWrapper
from Library.excel import read_locators

class Add_Opportunity:
    locators = read_locators("addoppor")
    # print(locators)

    def __init__(self,driver):
        self.driver = driver

    def add_opp(self):
        a = SeleniumWrapper(self.driver)
        a.click_element(Add_Opportunity.locators["openoppor"])
        a.click_element(Add_Opportunity.locators["addoppor"])
        a.send_data(Add_Opportunity.locators["orgname"],"TYSS")
        a.click_element(Add_Opportunity.locators["Relatedto"])
        a.win_handle(1)
        a.click_element(Add_Opportunity.locators["selectop"])
        a.win_handle(0)
        a.dropdwon(Add_Opportunity.locators["industry"],"Organizations")
        a.click_element(Add_Opportunity.locators["save"])