"""
Global variables

By design, import no any other local module inside this file.
Vice verse, it'd produce circular dependent imports.

action_config params:
  - comment: True or False if we comment on posts
  - comment_percentage: the % amount we comment on each post
  - follow_times: the number of times we follow a user
  - follow: True or False if we follow
  - follow_percentage: the % amount we follow
  - like: True or False if we like posts
  - like_percentage: the % amount we like
  - like_dont: list of words if matches we don't like
  - story: True or False if we watch stories
  - story_percentage: the % amount we watch stories
  - mandatory_language: post need to be in certain char set
  - user_interact_amount: the amount we interact with user
  - user_interact_random: the posts we select are random or not
  - user_interact_percentage: the % amount we interact
  - user_interact_media: the type of media we interact with

action_delays params: how much to wait in between each actions
  - enabled: True or False if we do actions delays
  - like: amount of time after a like
  - comment: amount of time after a comment
  - follow: amount of time after a follow
  - unfollow: amount of time after a unfollow
  - story: amount of time after each reel
  - randomize: True or False if we randomize actions delays
  - random_range: [ % min, % max] to randomize in between

quota_supervisor params: how much actions we do in an hour/per day
  - enabled: True or False if we do quota supervision
  - peak_likes: max amount per hour and per 24 hours
  - peak_follows: max amount per hour and per 24 hours
  - peak_unfollows: max amount per hour and per 24 hours
  - peak_server_calls: max amount per hout and per 24 hours

relationship_bounds:
    - enabled: True or False if we check the user
    - potency ratio: The ratio between followers/following
    - max_followers: the amount of followers the user should not be above
    - min_followers: the min amount of followers the user should have
    - min_following: the min amount of followings the user should have
    - min_posts: the min amount of posts the user should have

- hashtags: list of hashtags to look at
- users: list of users to look at
- comments: the list of possible comment
- locations: the lost of location to look at
- ignore_users: the one we don't interact with
- mandatory_words: we like if they are present
- ignore_if_contains: we don't like if contains
- dont_unfollow: the one we don't unfollow

"""

# objects import
import random

from instappium.common import Logger


class Settings:
    """ Globally accessible settings throughout whole project """

    # locations
    log_location = None
    database_location = None

    # set current profile credentials for DB operations
    profile = {"id": None, "name": None}

    # store user-defined delay time to sleep after doing actions
    # set defaults for all variables
    action_delays = {
        "enabled": True,
        "like": 150,
        "follow": 150,
        "unfollow": 150,
        "story": 150,
        "randomize": True,
        "random_range": [70, 140],
        "safety_match": False,
    }

    action_config = {}
    quota_supervisor = {
        "enabled": True,
        "peak_likes": [40, 300],
        "peak_follows": [25, 150],
        "peak_unfollows": [60, 200],
        "peak_server_calls": [300, 2500],
    }

    relationship_bounds = {
        "enabled": True,
        "potency_ratio": None,
        "max_followers": 3000,
        "min_followers": 25,
        "min_following": 25,
        "min_posts": 10,
    }
    hashtags = []
    users = []
    locations = []
    comments = []
    ignore_users = []
    mandatory_words = []
    ignore_if_contains = []
    dont_unfollow = []

    @classmethod
    def set_quota_supervisor(
        cls,
        enabled: bool = False,
        peak_likes: int = None,
        peak_follows: int = None,
        peak_unfollows: int = None,
        peak_server_calls: [] = None,
    ):
        cls.quota_supervisor["enabled"] = enabled
        cls.quota_supervisor["peak_likes"] = peak_likes
        cls.quota_supervisor["peak_follows"] = peak_follows
        cls.quota_supervisor["peak_unfollows"] = peak_unfollows
        cls.quota_supervisor["peak_server_calls"] = peak_server_calls

    @classmethod
    def set_relationship_bounds(
        cls,
        enabled: bool = False,
        potency_ratio: float = None,
        max_followers: int = None,
        min_followers: int = None,
        min_following: int = None,
        min_posts: int = None,
    ):
        cls.relationship_bounds["enabled"] = enabled
        cls.relationship_bounds["potency_ratio"] = potency_ratio
        cls.relationship_bounds["max_followers"] = max_followers
        cls.relationship_bounds["min_followers"] = min_followers
        cls.relationship_bounds["min_following"] = min_following
        cls.relationship_bounds["min_posts"] = min_posts

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
        random_range: [] = None,
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
        cls.action_delays["random_range"] = random_range
        cls.action_delays["safety_match"] = safety_match

    @classmethod
    def get_action_delays(cls):
        return cls.action_delays

    @classmethod
    def action_delay(cls, action: str):
        if not cls.action_delays["enabled"]:
            return 0
        else:
            return random.uniform(
                cls.action_delays[action] * cls.action_delays["random_range"][0] / 100,
                cls.action_delays[action] * cls.action_delays["random_range"][1] / 100,
            )

    @classmethod
    def set_hashtags(cls, hashtags: []):
        cls.hashtags = hashtags

    @classmethod
    def get_hashtags(cls):
        return cls.hashtags

    @classmethod
    def set_users(cls, users: []):
        cls.users = users

    @classmethod
    def get_users(cls):
        return cls.users

    @classmethod
    def set_locations(cls, locations: []):
        cls.locations = locations

    @classmethod
    def get_locations(cls):
        return cls.locations

    @classmethod
    def set_do_comment(cls, enabled: bool = False, percentage: int = 0):
        """
        Defines if images should be commented or not.
        E.g. percentage=25 means every ~4th picture will be commented.
        """

        cls.action_config["comment"] = enabled
        cls.action_config["comment_percentage"] = percentage

    @classmethod
    def get_action_config(cls):
        return cls.action_config

    @classmethod
    def set_comments(cls, comments: list):
        """
        Sets the possible posted comments.
        'What an amazing shot :heart_eyes: !' is an example for using emojis.
        """

        cls.comments = comments

    @classmethod
    def get_comments(cls):
        return cls.comments

    @classmethod
    def set_do_follow(cls, enabled: bool = False, percentage: int = 0, times: int = 1):
        """Defines if the user of the liked image should be followed"""

        cls.action_config["follow_times"] = times
        cls.action_config["follow"] = enabled
        cls.action_config["follow_percentage"] = min(percentage, 100)

    @classmethod
    def set_do_like(cls, enabled: bool = False, percentage: int = 0):

        cls.action_config["like"] = enabled
        cls.action_config["like_percentage"] = min(percentage, 100)

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
        cls.action_config["story"] = enabled
        cls.action_config["story_percentage"] = min(percentage, 100)

    @classmethod
    def set_dont_like(cls, tags: list):
        """Changes the possible restriction tags, if one of this
         words is in the description, the image won't be liked but user
         still might be unfollowed"""

        cls.action_config["like_dont"] = tags

    @classmethod
    def set_mandatory_words(cls, tags: list):
        """Changes the possible restriction tags, if all of this
         hashtags is in the description, the image will be liked"""

        cls.mandatory_words = tags

    @classmethod
    def get_mandatory_words(cls):
        return cls.mandatory_words

    @classmethod
    def set_user_interact(
        cls,
        amount: int = 10,
        percentage: int = 100,
        randomize: bool = False,
        media: str = None,
    ):
        """Define if posts of given user should be interacted"""

        cls.action_config["user_interact_amount"] = amount
        cls.action_config["user_interact_random"] = randomize
        cls.action_config["user_interact_percentage"] = percentage
        cls.action_config["user_interact_media"] = media

    @classmethod
    def set_ignore_users(cls, users: list):
        """Changes the possible restriction to users, if a user who posts
        is one of these, the image won't be liked"""

        cls.ignore_users = users

    @classmethod
    def get_ignore_users(cls):
        return cls.ignore_users

    @classmethod
    def set_ignore_if_contains(cls, words: list):
        """Ignores the don't likes if the description contains
        one of the given words"""

        cls.ignore_if_contains = words

    @classmethod
    def get_ignore_if_contains(cls):
        return cls.ignore_if_contains

    @classmethod
    def set_dont_include(cls, friends: list = None):
        """Defines which accounts should not be unfollowed"""
        cls.dont_unfollow = friends

    @classmethod
    def get_dont_unfollow(cls):
        return cls.dont_unfollow

    # @classmethod
    # def set_switch_language(cls, option: bool = True):
    #     cls.switch_language = option

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

        cls.action_config["mandatory_language"] = enabled
        cls.action_config["mandatory_character"] = char_set
