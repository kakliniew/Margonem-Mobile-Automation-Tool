
from OpencvActions import *
from SeleniumActions import *
from WebdriverWrapper import *


class MargoBot:
    def __init__(self):
        self.driver = WebdriverWrapper()
        self.sel_act = SeleniumActions(self.driver.driver)
        self.cv_act = OpencvActions(self.driver.driver)
        self.timeout = 3
        self.running = True
        self.default_screenshot_path = 'screenshots/actualView.png'

    def main_loop(self):
        self.get_to_loginpage_and_login()
        if not self.skip_appearing_window_and_get_to_the_battle():
            self.check_if_captcha_and_resolve()
            self.skip_appearing_window_and_get_to_the_battle()
        while self.running:
            if not self.find_element_and_click('images/autobutton.png', 0.4):
                if not self.check_if_captcha_and_resolve():
                    if not self.check_if_stamina_gone_and_end():
                        break
                self.find_element_and_click('images/autobutton.png', self.timeout)
            self.wait_for_end_of_batte_to_be_visible_for_time(0.3)
            self.check_if_low_hp_and_heal()
            self.find_element_and_click('images/nextbattle.png', self.timeout)


    def find_element_and_click(self, path, timeout):
        found_elements = self.cv_act.find_elements_from_image_with_wait(path, self.default_screenshot_path, timeout)
        if found_elements:
            self.sel_act.click_with_max_retries(found_elements, 3)
            return True
        else:
            return False

    def find_elements_and_click_first(self, path, timeout):
        found_elements = self.cv_act.find_elements_from_image_with_wait(path, self.default_screenshot_path, timeout)
        self.sel_act.click_element(found_elements[0])

    def wait_for_end_of_batte_to_be_visible_for_time(self, timeout):
        found_elements = self.cv_act.find_elements_from_image_with_wait('images/zwyciestwo.png',
                                                                        'screenshots/actualView.png', timeout)
        count_founds = len(found_elements)
        if count_founds > 0:
            print("Element from " + "'images/zwyciestwo.png'" + " was found")
        else:
            print("Element from " + "'images/zwyciestwo.png'" + " couldn't be find, looking for 'przegrana'")
            self.cv_act.find_elements_from_image_with_wait('images/przegrana.png', 'screenshots/actualView.png',
                                                           timeout)


    def send_keys_and_confirm(self, text):
        self.sel_act.send_keys(text)
        self.find_element_and_click('images/keyboardOK.png', self.timeout)

    def refill_arrows(self):
        pass

    def heal_the_character(self):
        self.find_elements_and_click_first('images/potion.png', self.timeout)
        self.find_element_and_click('images/uzyj_przedmiot.png', self.timeout)

    def resolve_captcha(self):
        to_search = None
        print("wykryto captcha, proba rozwiazania")
        if self.cv_act.is_element_visible_after_seconds('images/arcymagnaszyjniki.png', self.default_screenshot_path,
                                                        0.2):
            to_search = 'naszyjnik'
        elif self.cv_act.is_element_visible_after_seconds('images/arcymagmiecze.png', self.default_screenshot_path,
                                                          0.2):
            to_search = 'miecz'
        elif self.cv_act.is_element_visible_after_seconds('images/arcymagrekawice.png', self.default_screenshot_path,
                                                          0.2):
            to_search = 'rekawice'
        elif self.cv_act.is_element_visible_after_seconds('images/arcymagkaptury.png', self.default_screenshot_path,
                                                          0.2):
            to_search = 'helm'
        elif self.cv_act.is_element_visible_after_seconds('images/arcymagbuty.png', self.default_screenshot_path, 0.2):
            to_search = 'buty'
        elif self.cv_act.is_element_visible_after_seconds('images/arcymagpierscienie.png', self.default_screenshot_path,
                                                          0.2):
            to_search = 'pierscien'
        elif self.cv_act.is_element_visible_after_seconds('images/arcymagplaszcz.png', self.default_screenshot_path,
                                                          0.2):
            to_search = 'plaszcz'

        print("to search " + to_search)
        found_elements = self.cv_act.find_elements_from_image_with_wait('images/' + to_search + '.png',
                                                                        self.default_screenshot_path, self.timeout)
        empty_places = self.cv_act.find_elements_from_image_with_wait('images/slotarcymag.png',
                                                                      self.default_screenshot_path, self.timeout)
        print("znalezione elementy" + found_elements)
        print("znalezione puste miesjsca " + empty_places)
        for i in range(empty_places):
            self.sel_act.hold_and_moveto(found_elements[i], empty_places[i])

    def get_to_loginpage_and_login(self):
        self.find_element_and_click('images/wroc.png', self.timeout)
        self.find_element_and_click('images/loginpage.png', self.timeout)
        self.find_element_and_click('images/loginfield.png', self.timeout)
        self.send_keys_and_confirm(self.driver.userName)
        self.find_element_and_click('images/passfield.png', self.timeout)
        self.send_keys_and_confirm(self.driver.password)
        self.find_element_and_click('images/loginbutton.png', self.timeout)

    def skip_appearing_window_and_get_to_the_battle(self):
        if not self.find_element_and_click('images/brakustawienok.png', self.timeout):
            return False
        self.find_element_and_click('images/heroname.png', self.timeout)
        self.find_element_and_click('images/expmap.png', self.timeout)
        return True

    def check_if_captcha_and_resolve(self):
        if self.cv_act.is_element_visible_after_seconds('images/arcymag.png', self.default_screenshot_path, 0.2):
            self.resolve_captcha()
            return True
        else:
            if self.cv_act.is_element_visible_after_seconds('images/pierscien.png', self.default_screenshot_path, 0.2):
                self.resolve_captcha()
                return True
            else:
                return False

    def check_if_low_hp_and_heal(self):
        bgr = self.cv_act.get_color_of_pixel(self.default_screenshot_path, 215, 445)
        print(bgr)
        while bgr[0] != 17 and bgr[1] != 17 and bgr[2] != 167 and bgr[0] != 10 and bgr[1] != 10 and bgr[2] != 102:
            self.heal_the_character()
            sleep(1)
            bgr = self.cv_act.get_color_of_pixel(self.default_screenshot_path, 215, 445)
            print(bgr)

    def check_if_stamina_gone_and_end(self):
        if self.cv_act.is_element_visible_after_seconds('images/brakstaminy2.png', self.default_screenshot_path, 0.3):
            self.running = False
            print("zakonczono z powodu braku staminy")
        elif self.cv_act.is_element_visible_after_seconds('images/brakstaminy.png', self.default_screenshot_path, 0.2):
            self.running = False
            print("zakonczono z powodu braku staminy - komunikat drugi")
        else:
            self.running = False
            print("Dziwny stan aplikacji, nie rozpoznano")
        return False
