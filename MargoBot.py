
from OpencvActions import *
from SeleniumActions import *
from WebdriverWrapper import *


class MargoBot:
    def __init__(self):
        self.driver = WebdriverWrapper()
        self.sel_act = SeleniumActions(self.driver.driver)
        self.cv_act = OpencvActions(self.driver.driver)
        self.timeout = 10
        self.running = True
        self.default_screenshot_path = 'screenshots/actualView.png'

    def main_loop(self):
        self.get_to_loginpage_and_login()
        self.find_element_and_click('images/brakustawienok.png', self.timeout)
        self.find_element_and_click('images/heroname.png', self.timeout)
        self.find_element_and_click('images/expmap.png', self.timeout)
        while self.running:
            self.find_element_and_click('images/autobutton.png', self.timeout)
            if self.cv_act.is_element_visible_after_seconds('images/keyboardOK.png', self.default_screenshot_path, 0.5):
                self.heal_the_character()
            self.find_element_and_click('images/nextbattle.png', self.timeout)
            if self.cv_act.is_element_visible_after_seconds('images/brakstaminy.png', self.default_screenshot_path,
                                                            0.5):
                self.running = False
        time.sleep(2)
        self.driver.driver.save_screenshot('screenshots/newlocation.png')



    def find_element_and_click(self, path, timeout):
        found_elements = self.cv_act.find_elements_from_image_with_wait(path, self.default_screenshot_path, timeout)
        print("Found elements to click: ", found_elements)
        self.sel_act.click_with_max_retries(found_elements, 3)

    # def wait_for_element_to_be_visible_for_time(self, path, timeout):
    #     found_elements = self.cv_act.find_elements_from_image_with_wait(path, 'screenshots/actualView.png', timeout)
    #     count_founds = len(found_elements)
    #     if count_founds > 0:
    #         print("Element from " + path + " was found")
    #     else:
    #         print("Element from " + path + " couldn't be find, trying to repair...")
    #         self.repair_function()

    def repair_function(self):
        pass

    def send_keys_and_confirm(self, text):
        self.sel_act.send_keys(text)
        self.find_element_and_click('images/keyboardOK.png', self.timeout)

    def refill_arrows(self):
        pass

    def heal_the_character(self):
        pass

    def resolve_captcha(self):
        pass

    def get_to_loginpage_and_login(self):
        self.find_element_and_click('images/wroc.png', self.timeout)
        self.find_element_and_click('images/loginpage.png', self.timeout)
        self.find_element_and_click('images/loginfield.png', self.timeout)
        self.send_keys_and_confirm(self.driver.userName)
        self.find_element_and_click('images/passfield.png', self.timeout)
        self.send_keys_and_confirm(self.driver.password)
        self.find_element_and_click('images/loginbutton.png', self.timeout)
