from SeleniumActions import *
from OpencvActions import *
import time


class MargoBot:
    def __init__(self):
        self.sel_act = SeleniumActions()
        self.cv_act = OpencvActions()


    def start_exp(self):
        self.sel_act.open_app()
        time.sleep(5)
        self.sel_act.on_quit()

