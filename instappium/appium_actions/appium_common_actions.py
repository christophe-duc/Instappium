"""
Class to define the specific actions for the Common class to work with Appium
"""

# libraries import
import threading
from time import sleep
import random

# class import
from ..common import xpath, User, Logger


class AppiumCommonActions(object):
    """
    class for all the common actions (not related to user, comment, post, story)
    """

    def _scroll(self, amount):
        # we should find max boundaries of the screen
        # and randomly select the starting, ending point

        init_x = int(self.driver.DISPLAYSIZE["width"] * random.gauss(0.5, 0.1))
        init_y = random.int(0, self.driver.DISPLAYSIZE["height"] - amount)

        self.driver.swipe(init_x, init_y, init_x, init_y + amount)

    def go_profile(self):
        """
        user the action bar to go to the user profile
        :return:
        """
        profile = self.driver.find_elements_by_xpath(
            xpath.read_xpath("action_bar", "profile")
        )
        profile[0].click()

        user: User = self.get_userdata()

        return {"status": True, "user": user}

    def go_search(self, item: str, search_type: str):
        """
        go into the search tab
        :param item: what we want to search for
        :param search_type: accounts, hashtags or places
        :return:
        """
        # go into the search tab
        elem = self.driver.find_elements_by_xpath(
            xpath.read_xpath("action_bar", "search")
        )
        elem[0].click()
        sleep(3)

        elem = self.driver.find_elements_by_id(
            xpath.read_xpath("search", "search_text")
        )
        elem[0].click()
        sleep(1)

        elem = self.driver.find_elements_by_id(
            xpath.read_xpath("search", "search_text")
        )
        # we might want to open the keyboard and do a sendkey on that
        # self.simulate_typing(elem[0], item)
        elem[0].send_keys(item)
        sleep(3)
        # self.driver.hide_keyboard()

        elem = self.driver.find_elements_by_xpath(
            xpath.read_xpath("search", search_type)
        )

        elem[0].click()
        sleep(3)

        found_items = self.driver.find_elements_by_id(
            xpath.read_xpath("search", search_type + "_results")
        )

        for f_item in found_items:
            print("item=" + f_item.text)
            if f_item.text.lower().replace("#", "") == item:
                f_item.click()
                sleep(5)

                if search_type != "accounts":
                    # click on recent posts
                    # click on first post to be in feed mode
                    elem = self.driver.find_elements_by_id(
                        xpath.read_xpath("search", "recent")
                    )
                    elem[0].click()
                    sleep(5)

                    # find first post
                    elem = self.driver.find_elements_by_id(
                        xpath.read_xpath("search", "post_image_list")
                    )
                    elem[0].click()
                    sleep(5)

                return {"status": True}

        # we haven't found anything
        Logger.logerror("no item={} of type={} found".format(item, search_type))
        return {"status": False}

    def go_back(self):
        elem = self.driver.find_elements_by_id(xpath.read_xpath("action_bar", "back"))
        if len(elem) != 0:
            elem[0].click()

    def go_home(self):
        elem = self.driver.find_elements_by_xpath(
            xpath.read_xpath("action_bar", "home")
        )
        if len(elem) != 0:
            elem[0].click()

    def go_activity(self):
        elem = self.driver.find_elements_by_xpath(
            xpath.read_xpath("action_bar", "activity")
        )
        if len(elem) != 0:
            elem[0].click()

    def keep_alive(self):
        thread = threading.Thread(target=self._idle, args=())
        thread.daemon = True
        thread.start()

    def simulate_typing(self, elem: object, item: str):
        """
        a function to try to do a better job than send_keys
        """

    def _idle(self):
        while True:
            _ = self.driver.orientation
            sleep(20)
