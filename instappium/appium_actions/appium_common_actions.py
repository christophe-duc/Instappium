"""
Class to define the specific actions for the Common class to work with Appium
"""
# class import
from ..common.xpath import xpath
from ..common.model.user import User
from .helper_functions import _cleanup_count

# libraries import
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException


class AppiumCommonActions(object):
    """
    class for all the common actions (not related to user, comment, post, story)
    """

    def _get_userdata(self):
        """
        extract data from the user profile
        :return: a User object filled with the information we extracted
        """
        # we should add a layer in a DB to keep what we have already seen
        # so it acts as a kind of a cache
        # we can decide to refresh once in a while


        elem = self.driver.find_elements_by_id(xpath.read_xpath("profile", "username"))
        if len(elem) == 0:
            elem = self.driver.find_elements_by_id(xpath.read_xpath("profile", "username_back"))

        username = elem[0].text
        print(username)
        posts = _cleanup_count(self.driver.find_elements_by_id(xpath.read_xpath("profile", "posts"))[0].text)
        followers = _cleanup_count(self.driver.find_elements_by_id(xpath.read_xpath("profile", "followers"))[0].text)
        following = _cleanup_count(self.driver.find_elements_by_id(xpath.read_xpath("profile", "following"))[0].text)
        full_name = self.driver.find_elements_by_id(xpath.read_xpath("profile", "fullname"))[0].text

        elem = self.driver.find_elements_by_id(xpath.read_xpath("profile", "bio"))
        if len(elem) != 0:
            bio = elem[0].text
        else:
            bio = ''

        elem = self.driver.find_elements_by_id(xpath.read_xpath("profile", "category"))
        if len(elem) != 0:
            category = elem[0].text
        else:
            category = ''

        return User(username=username,
                    post_count=posts,
                    follower_count=followers,
                    following_count=following,
                    full_name=full_name,
                    bio=bio,
                    category=category,
                    )

    def _scroll_down(self, amount):
        # we should find max boundaries of the screen
        # and randomly select the starting, ending point

        init_x = int(self.driver.DISPLAYSIZE['width'] * random.gauss(0.5, 0.1))
        init_y = random.int(0, self.driver.DISPLAYSIZE['height'] - amount)

        self.driver.swipe(init_x,
                          init_y,
                          init_x,
                          init_y + amount)

    def go_profile(self):
        """
        user the action bacr to go to the user profile
        :param driver:
        :return:
        """
        profile = self.driver.find_elements_by_xpath(xpath.read_xpath("action_bar", "profile"))
        profile[0].click()

        user: User = self._get_userdata()

        return {"status": True, "user": user}


    def go_search(self, item: str, search_type: str):
        """
        go into the search tab
        :param item: what we want to search for
        :param search_type: accounts, hashtags or places
        :return:
        """
        # go into the search tab
        elem = self.driver.find_elements_by_xpath(xpath.read_xpath("action_bar", "search"))
        elem[0].click()
        sleep(3)

        elem = self.driver.find_elements_by_id(xpath.read_xpath("search", "search_text"))
        elem[0].click()
        sleep(1)
        # we should use sendkeys here if possible
        elem = self.driver.find_elements_by_id(xpath.read_xpath("search", "search_text"))
        elem[0].send_keys(item)
        sleep(3)

        elem = self.driver.find_elements_by_xpath(xpath.read_xpath("search", search_type))

        elem[0].click()
        sleep(3)



        found_items = self.driver.find_elements_by_id(xpath.read_xpath("search", search_type+"_results"))

        for f_item in found_items:
            print('item=' + f_item.text)
            if f_item.text.lower().replace('#', '') == item:
                f_item.click()
                sleep(2)
                # get the data we can:

                if search_type == "accounts":
                    user: User = self._get_userdata()
                    return {"status": True, "user": user}

                else:
                    # in the case of hashtags and places we get a grid of posts
                    return {"status": True}

    def go_back(self):
        self.driver.find_elements_by_id(xpath.read_xpath("action_bar", "back"))[0].click()
