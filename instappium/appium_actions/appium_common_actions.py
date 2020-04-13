"""
Class to define the specific actions for the Common class to work with Appium
"""
# class import
from ..common.xpath import xpath
from ..common.model.user import User
# libraries import
from time import sleep
from .helper_functions import _cleanup_count

class AppiumCommonActions(object):
    """
    class for all the common actions (not related to user, comment, post, story)
    """

    def go_profile(self):
        """

        :param driver:
        :return:
        """
        profile = self.driver.find_elements_by_xpath(xpath.read_xpath("action_bar", "profile"))
        profile[0].click()

    def go_user(self, user: User = None):

        self._go_search()

        elem = self.driver.find_element_by_id(xpath.read_xpath("search", "search_text"))
        elem.click()
        sleep(2)
        elem.set_value(user.username)
        sleep(3)

        found_users = self.driver.find_elements_by_xpath(xpath.read_xpath("search", "search_user_results"))

        for f_user in found_users:
            if f_user.text == user.username:
                f_user.click()
                sleep(2)
                # get the data we can:
                posts = self.driver.find_element_by_id(xpath.read_xpath("profile", "posts"))
                print(posts.text)
                user.post_count = _cleanup_count(posts.text)

                followers = self.driver.find_element_by_id(xpath.read_xpath("profile", "followers"))
                print(followers.text)
                user.follower_count = _cleanup_count(followers.text)

                following = self.driver.find_element_by_id(xpath.read_xpath("profile", "following"))
                print(following.text)
                user.following_count = _cleanup_count(following.text)

                print(user)
                return {"status": True}

        return {"status": False, "error": 'Unable to find user: {} did you request the right name?'.format(user.username)}

        # searching on the app is the way to move from one user to another
        # if the list is not null then we should click on it to go to that user

    def go_down(self, amount):
        # we should find max boundaries of the screen
        # and randomly select the starting, ending point

        init_x=int(self.driver.DISPLAYSIZE['width']*random.gauss(0.5, 0.1))
        init_y=random.int(0,self.driver.DISPLAYSIZE['height']-amount)

        self.driver.swipe(init_x,
                              init_y,
                              init_x,
                              init_y+amount)

    def _go_search(self):
        elem = self.driver.find_elements_by_xpath(xpath.read_xpath("action_bar", "search"))
        elem[0].click()
        sleep(2)
