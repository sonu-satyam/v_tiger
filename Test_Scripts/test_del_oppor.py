from POM.login import Login
from POM.delOppor import DelOppor

def test_del_opportunity(_driver):
    login = Login(_driver)
    login.login()

    delete_ = DelOppor(_driver)
    delete_.del_oppor()
