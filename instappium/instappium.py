"""Instappium main class"""

from .appium_webdriver import AppiumWebDriver
from .common.xpath import xpath
from instappium.common import Logger

from time import sleep

class InstAppium:
    """
    Class to be instantiated to use the script
    """
    _webdriver = None

    def __init__(self, username: str = None, password: str = None, device: str = None):
        """
        basic initialization
        """
        self._username = username
        self._password = password
        self._device = device

        try:
            self._webdriver = AppiumWebDriver(devicename=device)
        except:
            Logger.error("Could not create webdriver; please make sure Appium is running")
            quit()

        current_activity = self._webdriver.current_activity().split('.')[-1]

        # Lets log in!
        if 'SignedOut' in current_activity:
            check_login = self._webdriver.find_elements_by_xpath(xpath.read_xpath("login","login_button"))
            check_login[0].click()

            username_edit_text = self._webdriver.find_elements_by_xpath(xpath.read_xpath("login","login_username"))
            username_edit_text[0].set_value(username)

            password_edit_text = self._webdriver.find_elements_by_xpath(xpath.read_xpath("login","login_password"))
            password_edit_text[0].set_value(password)
            sleep(1)

            log_in = self._webdriver.find_elements_by_xpath(xpath.read_xpath("login","log_me_in"))
            log_in[0].click()

            if self._webdriver.current_activity().split('.')[-1] == 'MainActivity':
                print('Succesfully Logged in!')

    def main(self):
        self._webdriver.swipe(0, 0, 0, 100, 100)
