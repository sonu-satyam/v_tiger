from POM.login import Login
from Library.lib import SeleniumWrapper
import pytest

@pytest.mark.smoke_test
def test_login(driver_):
    # print(driver_)
    a = SeleniumWrapper(driver_)
    login = Login(driver_)
    login.login()



