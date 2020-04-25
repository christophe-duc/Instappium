"""
Class to define the specific actions for the User class to work with Appium
"""
from .helper_functions import _cleanup_count
from ..common import xpath, User, Settings


class AppiumUserActions:
    """"
    Implementation class for User
    """

    def get_userdata(self):
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
        posts = _cleanup_count(self.driver.find_elements_by_id(xpath.read_xpath("profile", "posts"))[0].text)
        followers = _cleanup_count(self.driver.find_elements_by_id(xpath.read_xpath("profile", "followers"))[0].text)
        following = _cleanup_count(self.driver.find_elements_by_id(xpath.read_xpath("profile", "following"))[0].text)
        print("following={}".format(following))
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

    def follow_user(self):
        """
        Follow a user
        :return:
        """
        elem = self.driver.find_elements_by_xpath(xpath.read_xpath('profile', 'following_button'))
        elem[0].click()

        # we should check here that we don't have a block before returning
        # if look for block, then.... return {'status': False}
        Settings.action_delay('follow')

        return {'status': True}

    def unfollow_user(self):
        """
        Unfollow a user
        :return:
        """
        elem = self.driver.find_elements_by_xpath(xpath.read_xpath('profile', 'unfollowing_button'))
        elem[0].click()

        # we should check here that we don't have a block before returning
        # if look for block, then.... return {'status': False}
        Settings.action_delay('unfollow')

        return {'status': True}

    def is_followed(self):
        """
        respond true or false if the user is already followed
        :return:
        """
        elem = self.driver.find_elements_by_xpath(xpath.read_xpath('profile', 'following_button'))
        if len(elem) > 0:
            return True
        else:
            return False

