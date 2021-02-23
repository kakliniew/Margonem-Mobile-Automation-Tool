from appium.webdriver.common.touch_action import TouchAction
import time
from random import *
from selenium.common.exceptions import StaleElementReferenceException


class SeleniumActions:
    def __init__(self, driver):
        self.driver = driver

    def click_with_max_retries(self, list_of_cords, max_retries):
        for i in range(max_retries):
            try:
                self.click_elements(list_of_cords)
                break
            except StaleElementReferenceException:
                print("Ooops couldn't click that")



    def click_elements(self,list_of_cords):
        for cord in list_of_cords:
            time.sleep(random())
            TouchAction(self.driver).tap(None, cord[0], cord[1], 1).perform()
            print("Clicked element x = ", cord[0], "y = ", cord[1])
