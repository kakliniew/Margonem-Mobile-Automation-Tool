# MargonemMobileBot
This is a proof-of-concept application. It performs test automation of a mobile application created in Unity. 
It is not possible to locate elements of the application using selectors, so the program created uses finding "template" in screenshot (OpenCv match template). Some of the commands are passed via adb shell. 

# Requirements
  * Python 3.7+
  * Nox Player 
  * Appium
  * Numpy
  * OpenCv2
  * TouchAction
  * adb

# Configuration

### Nox Player and adb
1. Install Nox Player
1. Run emulator
1. In Nox settings:
 `General settings -> Root` and 
  `Performance settings -> mobile phone and 1080x1920`
1. Steps described here: [Instruction](https://www.bignox.com/blog/how-to-connect-android-studio-with-nox-app-player-for-android-development-and-debug/)
1. Check if there is a connection between Emulator and adb -> type `adb devices` in console(should return `127.0.0.1:62001 device`)
1. Install Margonem Mini from Google Apps

### Code 
1. Set your credentials in credentials.yaml
1. Replace 'heroname.png', 'expmap.png' and 'potion.png' in '/images/' with images cut from screenshots taken manually in Nox


# Launch
1. Start Nox Player
1. Check if there is a connection between Emulator and adb -> type `adb devices` in console(should return `127.0.0.1:62001 device`)
1. Start appium
1. Start Margobot with `python3 app.py`
