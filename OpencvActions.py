import cv2
import numpy as np


class OpencvActions:
    def __init__(self, driver):
        self.__driver = driver

    @staticmethod
    def find_matches(screenshot, template, threshold):
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        count = 0
        points = []
        # Counts the matches themselves
        # and saves their centers to an array
        for pt in zip(*loc[::-1]):
            count = count + 1
            points.append((pt[0] + w / 2, pt[1] + h / 2))
        print(count, " match(es) found.")
        return points

    def find_elements_from_image_with_wait(self, loading_img_path, loading_scrn_path, timeout=30):
        load_img = cv2.imread(loading_img_path, 0)  # Loading Image
        time_spent = 0
        count_founds = 0
        found_points = None
        delay_time = .10
        while time_spent + 0.05 <= timeout and count_founds == 0:
            # Save a screenshot of the screen
            self.__driver.save_screenshot(loading_scrn_path)
            print("Screenshot saved")
            print("Looking for Element " + loading_img_path)
            load_scrn = cv2.imread(loading_scrn_path, 0)  # Loading Screenshot
            found_points = self.find_matches(load_scrn, load_img, 0.99)
            count_founds = len(found_points)
            # sleep(delay_time)
            time_spent += delay_time
        if time_spent + 0.05 >= timeout and count_founds == 0:
            print("Couldn't find the element for ", time_spent, " seconds!")
        else:
            print("Element(s) found in ", time_spent, " seconds.")
        return found_points

    def get_color_of_pixel(self, loading_scrn_path, cord_x, cord_y):
        self.__driver.save_screenshot(loading_scrn_path)
        load_img = cv2.imread(loading_scrn_path)
        return load_img[cord_x][cord_y]

    def is_element_visible_after_seconds(self, loading_img_path, loading_scrn_path, timeout=30):
        return self.find_elements_from_image_with_wait(loading_img_path, loading_scrn_path, timeout)
