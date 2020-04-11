"""
Global variables

By design, import no any other local module inside this file.
Vice verse, it'd produce circular dependent imports.
"""

# objects import
from instappium.common import Logger

class Settings:
    """ Globally accessible settings throughout whole project """

    # locations
    log_location = None
    database_location = None

    # set current profile credentials for DB operations
    profile = {"id": None, "name": None}

    # hold live Quota Supervisor configuration for global usage
    QS_config = {}

    # store user-defined delay time to sleep after doing actions
    action_delays = {}

    # store configuration of text analytics
    meaningcloud_config = {}
    yandex_config = {}

    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    )

    # state of instantiation of InstaPy
    InstAppium_is_running = False

    devicename = None
    devicetimeout = None
    client_host = None
    client_port = None

    @classmethod
    def set_action_delays(
        cls,
        enabled: bool = False,
        like: int = None,
        comment: int = None,
        follow: int = None,
        unfollow: int = None,
        story: int = None,
        randomize: bool = False,
        random_range_from: int = None,
        random_range_to: int = None,
        safety_match: bool = True,
    ):
        """ Set custom sleep delay after actions """
        cls.action_delays["enabled"] = enabled
        cls.action_delays["like"] = like
        cls.action_delays["comment"] = comment
        cls.action_delays["follow"] = follow
        cls.action_delays["unfollow"] = unfollow
        cls.action_delays["story"] = story
        cls.action_delays["randomize"] = randomize
        cls.action_delays["random_range_from"] = random_range_from
        cls.action_delays["random_range_to"] = random_range_to
        cls.action_delays["safety_match"] = safety_match

    @classmethod
    def set_do_comment(cls, enabled: bool = False, percentage: int = 0):
        """
        Defines if images should be commented or not.
        E.g. percentage=25 means every ~4th picture will be commented.
        """

        cls.do_comment = enabled
        cls.comment_percentage = percentage

    @classmethod
    def set_comments(cls, comments: list = [], media: str = None):
        """
        Sets the possible posted comments.
        'What an amazing shot :heart_eyes: !' is an example for using emojis.
        """

        if media not in [None, "Photo", "Video"]:
            Logger.warning('Unkown media type! Treating as "any".')
            media = None

        cls.comments = comments

        if media is None:
            cls.comments = comments
        else:
            attr = "{}_comments".format(media.lower())
            setattr(cls, attr, comments)

    @classmethod
    def set_do_follow(cls, enabled: bool = False, percentage: int = 0, times: int = 1):
        """Defines if the user of the liked image should be followed"""

        cls.follow_times = times
        cls.do_follow = enabled
        cls.follow_percentage = percentage

    @classmethod
    def set_do_like(cls, enabled: bool = False, percentage: int = 0):

        cls.do_like = enabled
        cls.like_percentage = min(percentage, 100)

    @classmethod
    def set_do_story(
        cls, enabled: bool = False, percentage: int = 0, simulate: bool = False
    ):
        """
            configure stories
            enabled: to add story to interact
            percentage: how much to watch
            simulate: if True, we will simulate watching (faster),
                      but nothing will be seen on the browser window
        """
        cls.do_story = enabled
        cls.story_percentage = min(percentage, 100)
        cls.story_simulate = simulate

    @classmethod
    def set_dont_like(cls, tags: list = []):
        """Changes the possible restriction tags, if one of this
         words is in the description, the image won't be liked but user
         still might be unfollowed"""

        if not isinstance(tags, list):
            Logger.warning("Unable to use your set_dont_like " "configuration!")
        else:
            cls.dont_like = tags

    @classmethod
    def set_mandatory_words(cls, tags: list = []):
        """Changes the possible restriction tags, if all of this
         hashtags is in the description, the image will be liked"""

        if not isinstance(tags, list):
            Logger.warning("Unable to use your set_mandatory_words " "configuration!")
        else:
            cls.mandatory_words = tags

    @classmethod
    def set_user_interact(
        cls,
        amount: int = 10,
        percentage: int = 100,
        randomize: bool = False,
        media: str = None,
    ):
        """Define if posts of given user should be interacted"""

        cls.user_interact_amount = amount
        cls.user_interact_random = randomize
        cls.user_interact_percentage = percentage
        cls.user_interact_media = media

    @classmethod
    def set_ignore_users(cls, users: list = []):
        """Changes the possible restriction to users, if a user who posts
        is one of these, the image won't be liked"""

        cls.ignore_users = users

    @classmethod
    def set_ignore_if_contains(cls, words: list = []):
        """Ignores the don't likes if the description contains
        one of the given words"""

        cls.ignore_if_contains = words

    @classmethod
    def set_dont_include(cls, friends: list = None):
        """Defines which accounts should not be unfollowed"""

        cls.dont_include = set(friends) or set()
        cls.white_list = set(friends) or set()

    @classmethod
    def set_switch_language(cls, option: bool = True):
        cls.switch_language = option

    @classmethod
    def set_mandatory_language(
        cls, enabled: bool = False, character_set: list = ["LATIN"]
    ):
        """Restrict the description of the image to a character set"""

        char_set = []

        if not isinstance(character_set, list):
            character_set = [character_set]

        for chr_set in character_set:
            if chr_set not in [
                "LATIN",
                "GREEK",
                "CYRILLIC",
                "ARABIC",
                "HEBREW",
                "CJK",
                "HANGUL",
                "HIRAGANA",
                "KATAKANA",
                "THAI",
                "MATHEMATICAL",
            ]:
                Logger.warning('Unkown character set! Treating as "LATIN".')
                ch_set_name = "LATIN"
            else:
                ch_set_name = chr_set

            if ch_set_name not in char_set:
                char_set.append(ch_set_name)

        cls.mandatory_language = enabled
        cls.mandatory_character = char_set


class Storage:
    """ Globally accessible standalone storage """

    # store realtime record activity data
    record_activity = {}
