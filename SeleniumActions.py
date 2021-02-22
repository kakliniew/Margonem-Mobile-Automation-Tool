from appium import webdriver

class SeleniumActions:
    def __init__(self):
        self.userName = "YOUR_USERNAME"
        self.accessKey = "YOUR_ACCESS_KEY"

        self.desired_caps = {
            "build": "Python Android",
            "device": "e66ef570",
            "appPackage": "com.garmory.mobilemargonem",
            "appActivity": "com.unity3d.player.UnityPlayerActivity",
            "app": "C:\\Users\\crump\\Documents\\studia opole\\margonem\MargoMini.apk",
            "platformName": "Android"
        }
        self.driver = None


    def open_app(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)


    def on_quit(self):
        self.driver.quit()
