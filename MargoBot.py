from SeleniumActions import *
from OpencvActions import *
from WebdriverWrapper import *
import time


class MargoBot:
    def __init__(self):
        self.driver = WebdriverWrapper()
        self.sel_act = SeleniumActions(self.driver.driver)
        self.cv_act = OpencvActions(self.driver.driver)
        self.timeout = 15

    def main_loop(self):
        self.find_element_and_click('images/wroc.png', self.timeout)
        self.wait_for_element_to_be_visible_for_time('images/loginpage.png', self.timeout)
        self.find_element_and_click('images/loginfield.png', self.timeout)
        self.send_keys_and_confirm(self.driver.userName)
        self.find_element_and_click('images/passfield.png', self.timeout)
        self.send_keys_and_confirm(self.driver.password)
        self.find_element_and_click('images/loginbutton.png', self.timeout)
        self.find_element_and_click('images/heroname.png', self.timeout)
        self.find_element_and_click('images/expmap.png', self.timeout)
        self.find_element_and_click('images/autobutton.png', self.timeout)
        self.find_element_and_click('images/nextbattle.png', self.timeout)
        self.find_element_and_click('images/autobutton.png', self.timeout)
        time.sleep(2)
        self.driver.driver.save_screenshot('screenshots/newlocation.png')



    def find_element_and_click(self, path, timeout):
        found_elements = self.cv_act.find_elements_from_image_with_wait(path, 'screenshots/actualView.png', timeout)
        print("Found elements to click: ", found_elements)
        self.sel_act.click_with_max_retries(found_elements, 3)

    def wait_for_element_to_be_visible_for_time(self, path, timeout):
        found_elements = self.cv_act.find_elements_from_image_with_wait(path, 'screenshots/actualView.png', timeout)
        count_founds = len(found_elements)
        if count_founds > 0:
            print("Element from " + path + " was found")
        else:
            print("Element from " + path + " couldn't be find, trying to repair...")
            self.repair_function()

    def repair_function(self):
        pass

    def send_keys_and_confirm(self, text):
        self.sel_act.send_keys(text)
        self.find_element_and_click('images/keyboardOK.png', self.timeout)