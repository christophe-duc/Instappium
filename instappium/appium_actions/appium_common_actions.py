"""
Class to define the specific actions for the Common class to work with Appium
"""
# class import

# libraries import
from time import sleep

class AppiumCommonActions(object):
    """
    class for all the common actions (not related to user, comment, post, story)
    """

    def go_profile(self):
        """

        :param driver:
        :return:
        """
        profile = self.webdriver_instance.find_elements_by_xpath("//android.widget.FrameLayout[@content-desc='Profile' and @index=4]")
        self.webdriver_instance.click(profile[0])

    def go_user(self,user):

        cls._go_search()

        elem = AppiumWebDriver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text")
        AppiumWebDriver.click(elem)
        sleep(2)
        elem.set_value(user.username)
        sleep(3)

        found_users = AppiumWebDriver.find_elements_by_xpath("//android.widget.TextView[@resource-id='com.instagram.android:id/row_search_user_username']")

        for f_user in found_users:
            if f_user.text == user.username:
                AppiumWebDriver.click(f_user)
                return True
        Logger.error('Unable to find user: {} did you request the right name?'.format(user.username))
        return False

        # searching on the app is the way to move from one user to another
        # if the list is not null then we should click on it to go to that user

    def go_down(self, amount):
        # we should find max boundaries of the screen
        # and randomly select the starting, ending point

        init_x=int(AppiumWebDriver.DISPLAYSIZE.width*random.gauss(0.5, 0.1))
        init_y=random.int(0,AppiumWebDriver.DISPLAYSIZE.height-amount)

        AppiumWebDriver.swipe(init_x,
                              init_y,
                              init_x,
                              init_y+amount)

    def _go_search(cls):
        elem = AppiumWebDriver.find_elements_by_xpath("//android.widget.FrameLayout[@content-desc='Search and Explore' and @index=1]")
        AppiumWebDriver.click(elem[0])
        sleep(2)
