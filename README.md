  <p align="center">
    <a href="https://github.com/timgrossmann/InstaPy/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/license-GPLv3-blue.svg" />
    </a>
    <a href="https://github.com/appium/appium">
      <img src="https://img.shields.io/badge/built%20with-Appium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
    <a href="https://travis-ci.org/christophe-duc/Instappium">
	<img src="https://travis-ci.org/christophe-duc/Instappium.svg?branch=master">
    </a>
  </p>

# Welcome to Instappium

This project is highly inspired and takes some of the code back from instapy (https://github.com/timgrossmann/InstaPy)
originally developped by Tim Grossmann and community

The goal of this project is to try to hide the automation behind a legitimate phone app, so it is easier to bypass any 
"easy" detection algorithm that may be done. It is also an attempt at not having a very detailed script that describe 
the actions to be done. Ideally we would like to let Instappium choose the actions it wants to do in a random manner 
and using the exact same flow as the app interface can provide so it is more natural.

Important note: the project is in heavy development at the moment so it is probably not fully usable or will crash a 
lot. There is no need to open issues/report, what we need is your help in fixing the code. So fork the repo and propose
a pull request that fix it. (https://guides.github.com/activities/forking/)

# Installation

You will need: 
1. Appium
2. an Android simulated device (for example using android studio and creating a device)
3. the app, you can find it on apkpure

# Qwick How to

2. Download and install [appium](https://github.com/appium/appium-desktop/releases/tag/v1.13.0)

3. Download and install [Andriod Studio](https://developer.android.com/studio)

4.  Download the [apk](https://apkpure.com/instagram/com.instagram.android/download/169474968-APK?from=variants%2Fversion)
  
    Note: make sure to map the correct apk variant with the CPU/ABI flavor of your android device

5. Start a new Android Studio (AS) project:
	- Launch AS
	- Click "Configure -> AVD Manager"
	
6.  Create a new emulator in the AVD manager by Click "Create Virtual Device" and follow it steps
7. Go to the android studio terminal (bottom of the screen): `cd C:\Users\YOUR NAME HERE\AppData\Local\Android\Sdk\platform-tools`  or whatever path you have to the `platform-tools` folder

8. Install the apk: `adb install [INSERT THE PATH TO YOUR DOWNLOADED INSTAGRAM APK]`

9. Add the `ANDROID_HOME` variable to your environment variables with path being the path to `[FULL PATH HERE]/Sdk/` mentioned in earlier steps

For Ubuntu: Dont use the symbol '~' in the path, because the appium parser doesnt seem to recognize it.

10. Start your appium server with default settings

11. Launch the emulator

12. Give it time for the emulator to setup everything (AS will stop showing messages in the bottom)

13. Make sure you enter the right device name on your test file (You can find it by running `adb devices` in the android terminal) along with your instagram credentials

14. Test your instappium
```python
import instappium

session = instappium.InstAppium(username='xxx', password='yyy', device='emulator-5554', show_logs=True)

session._webdriver.go_search('whoever you want', 'accounts')

# doing one action using the FSM
from instappium.engine import FSMSession
fsm = FSMSession(session._webdriver)

# should respond idle
fsm.state

# let's go to the home page
fsm.go_homepage()
```