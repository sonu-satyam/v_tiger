from POM.addopportunity import Add_Opportunity
from POM.login import Login
from Library.lib import SeleniumWrapper
from pytest import mark



# @mark.xfail
def test_add_oppor(_driver):
    a = SeleniumWrapper(_driver)
    login = Login(_driver)
    login.login()

    add_ = Add_Opportunity(_driver)
    add_.add_opp()

