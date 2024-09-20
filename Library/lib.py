from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def _wait(some_func):
    def wrapper(*args,**kwargs):
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver,15)
        w.until(ec.presence_of_element_located(locator))
        return some_func(*args,**kwargs)
    return wrapper



class SeleniumWrapper:

    def __init__(self,driver):
        self.driver = driver
    @_wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
    @_wait
    def send_data(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)
    @_wait
    def dropdwon(self,locator,data):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(data)

    @_wait
    def mouse_hover(self,locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @_wait
    def double_click(self,locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.double_click(element).perform()


    def win_handle(self,n):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[n])

    def pop_up_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def pop_up_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    @_wait
    def drag_drop(self,source_locator,target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element,target_element)

    def screen_shot(self):
        self.driver.save_screenshot("screenshot.png")

    def nothing(self):
        return "sonu gandu"

    def non(self):
        return "nothing"


