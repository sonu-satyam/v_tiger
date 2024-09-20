from POM.login import Login
from Library.lib import SeleniumWrapper

def test_login(_driver):
    a = SeleniumWrapper(_driver)
    login = Login(_driver)
    login.login()
