from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action = "store", default = "firefox")

@pytest.fixture(scope = "module")
def _driver(request):
    browser = request.config.getoption("--browser")
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("browser not supported")
    driver.get("http://49.249.28.218:8888/index.php?action=Login&module=Users")
    yield driver
    driver.close()

def func():
    return "akash"
