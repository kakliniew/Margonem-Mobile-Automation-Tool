import yaml
from appium import webdriver


class WebdriverWrapper:
    def __init__(self):
        self.userName = None
        self.password = None

        self.__desired_caps = {
            "appPackage": "com.garmory.mobilemargonem",
            "appActivity": "com.unity3d.player.UnityPlayerActivity",
            "app": "C:\\Users\\crump\\Documents\\studia opole\\margonem\MargoMini.apk",
            "platformName": "Android",
            "newCommandTimeout": "0"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.__desired_caps)
        self.__load_credentials()

    def __del__(self):
        self.driver.quit()

    def __load_credentials(self):
        with open("credentials.yaml", 'r') as stream:
            try:
                yaml_file = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                yaml_file = None
                print(exc)
        self.userName = yaml_file['username']
        self.password = yaml_file['password']
        print("Credentials correctly loaded")
