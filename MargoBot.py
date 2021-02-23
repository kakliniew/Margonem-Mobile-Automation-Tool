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

    def start_exp(self):
        time.sleep(5)
        self.find_element_and_click('images/wroc.png', self.timeout)
        time.sleep(5)

    def find_element_and_click(self, path, timeout):
        points = self.cv_act.find_elements_from_image_with_wait(path, 'screenshots/actualView.png', timeout)
        print("found points : ", points)
        self.sel_act.click_with_max_retries(points, 3)

