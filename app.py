# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.common.mobileby import MobileBy


#
# search_element = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
# )
# search_element.click()
#
# search_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
# )
# search_input.send_keys("BrowserStack")
#
#
# search_results = driver.find_elements_by_class_name("android.widget.TextView")
# assert(len(search_results) > 0)
#

from MargoBot import *

margo_bot = MargoBot()
margo_bot.main_loop()

