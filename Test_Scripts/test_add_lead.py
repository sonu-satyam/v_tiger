from pytest import mark

from POM.addlead import AddLead
from POM.login import Login
from Library.lib import SeleniumWrapper
from Library.excel import read_headers,read_data
headers = read_headers("test_add_lead","addleads")
data = read_data("test_add_lead", "addleads")

@mark.parametrize(headers,data)
def test_add_lead(_driver,salutation,fname,lname,company,designation,lead_source):
    a = SeleniumWrapper(_driver)
    login = Login(_driver)
    login.login()

    add_lead = AddLead(_driver)
    add_lead.create_lead(salutation,fname,lname,company,designation,lead_source)