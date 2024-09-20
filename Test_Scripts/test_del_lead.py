from POM.login import Login
from Library.lib import SeleniumWrapper
from POM.deletelead import DeleteLeads

def test_del_lead(_driver):
    a = SeleniumWrapper(_driver)
    login = Login(_driver)
    login.login()

    d = DeleteLeads(_driver)
    d.dellead()