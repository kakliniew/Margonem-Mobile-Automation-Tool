from appium import webdriver
import yaml


class WebdriverWrapper:
    def __init__(self):
        self.userName = None
        self.password = None

        self.desired_caps = {
            "build": "Python Android",
            "device": "e66ef570",
            "appPackage": "com.garmory.mobilemargonem",
            "appActivity": "com.unity3d.player.UnityPlayerActivity",
            "app": "C:\\Users\\crump\\Documents\\studia opole\\margonem\MargoMini.apk",
            "platformName": "Android"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        self.load_credentials()

    def __del__(self):
        self.driver.quit()


    def load_credentials(self):
        with open("credentials.yaml", 'r') as stream:
            try:
                yaml_file = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self.userName = yaml_file['username']
        self.password = yaml_file['password']
        print(self.password)
        print(self.userName)
