import subprocess
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
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
                sleep(1)

    def click_elements(self,list_of_cords):
        for cord in list_of_cords:
            # time.sleep(random())
            self.click_element(cord)

    def send_keys(self, text):
        command = "adb shell input text \"" + text + "\""
        subprocess.run(command)
        print("Text was sent")

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def press_ok(self):
        self.driver.press_keycode()

    def click_element(self, cords):
        TouchAction(self.driver).tap(None, cords[0], cords[1], 1).perform()
        print("Clicked element x = ", cords[0], "y = ", cords[1])

    def hold_and_moveto(self, cords_start, cords_end):
        TouchAction(self.driver).long_press(None, cords_start[0], cords_start[1]) \
            .move_to(None, cords_end[0], cords_end[1]).release().perform()
        sleep(0.2)
