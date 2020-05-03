"""
Class to create all necessary environment for the Finite State Machine
"""
# Library import
from transitions import Machine
import random

# Class import
from instappium.common import Logger
from ..common import Settings
from ..appium_webdriver import AppiumWebDriver


class FSMSession(object):
    """
    Define all the states and transitions, callbacks of an instagram session

    Inputs: a set of configuration (what actions, how much, scheduled)
    Output: the state machine will perform the amount of actions configured and scheduled

    You will have no exact control on when a specific action is going to be done or when
    everything is as random as possible

    """

    # all_possible_states
    states = [
        "homepage",
        "searchpage",
        "user" "activitypage",
        "profilepage",
        "commentpage",
        "storypage",
        "feed",
        "idle",
    ]

    # all possible transitions
    transitions = [
        {"trigger": "go_homepage", "source": "*", "dest": "homepage"},
        {"trigger": "go_searchpage", "source": "*", "dest": "searchpage"},
        {"trigger": "go_user", "source": "searchpage", "dest": "user"},
        {"trigger": "do_feed", "source": "searchpage", "dest": "feed"},
        # {'trigger': 'go_camera', 'source': '*', 'dest': 'camera_page'},
        {"trigger": "go_activitypage", "source": "*", "dest": "activitypage"},
        {"trigger": "go_profilepage", "source": "*", "dest": "profilepage"},
        {
            "trigger": "go_storypage",
            "source": ["homepage", "profilepage"],
            "dest": "storypage",
        },
        {"trigger": "go_idle", "source": "*", "dest": "idle"},
        {"trigger": "do_sleep", "source": "idle", "dest": "idle"},
    ]

    # expected actions_config parameters
    # { 'hashtags': ['#instagood', ...],
    #   'users': ['thisisbillgates', ... ],
    #   'locations': ['antartica', ...],
    #   'comments': ['this is a test', ...],
    #   'follow': True,
    #   'unfollow': True,
    #   'stories': True,
    #   'story_reactions': ['love','applause', ...]
    # }

    # currently safe default numbers
    # quota = {
    #     "peak_likes": (40, 400),
    #     "peak_comments":  (20, 200),
    #     "peak_follows": (20, 200),
    #     "peak_unfollows": (50, 200),
    # }

    def __init__(self, session: AppiumWebDriver):
        """
        Initialization of the FSM with what we want to do

        :param quota: the quota information
        :param actions: what we want to do
        :param session: the initialized AppiumWebDriver
        """
        # we should initialize the state machine according to the config
        # no need to have followed states if following is not configured

        print("auto-configure states and transitions here!")
        self.machine = Machine(
            model=self, states=self.states, transitions=self.transitions, initial="idle"
        )

        self.session = session
        # Keep a stack of previous states we can go back to with the back button
        self.stack_searchpage = []
        self.stack_homepage = []
        self.stack_activity = []
        # session stats
        self.followed = 0
        self.unfollowed = 0
        self.liked = 0
        self.commented = 0
        self.watched = 0

    def on_enter_homepage(self):
        """

        :return:
        """
        self.session.go_home()

    def on_exit_homepage(self):
        """

        :return:
        """

    def on_enter_searchpage(self):
        """
        Arrive on the searchpage and search for a user, hashtag, location etc, defined in settings
        :return:
        """
        # check and randomly take one from users, hashtags, locations

        possible_types = []

        # make sure we are at the top level
        while len(self.stack_searchpage) > 0:
            eval(self.stack_searchpage.pop())

        if len(Settings.get_locations()) > 0:
            possible_types.append("locations")

        if len(Settings.get_hashtags()) > 0:
            possible_types.append("hashtags")

        if len(Settings.get_users()) > 0:
            possible_types.append("users")

        search_type = random.choice(possible_types)
        item = random.choice(eval("Settings.get_" + search_type + "()"))

        res = self.session.go_search(item, search_type)
        self.stack_searchpage.append("self.session.go_back()")
        if res.status:
            self.stack_searchpage.append("self.session.go_back()")
            if search_type == "accounts":
                self.go_user()
            else:
                self.go_feed()
        else:
            # item was not found
            # we go back to idle?
            self.go_idle()

    def on_enter_user(self):
        user = self.session.get_userdata()

        # dump the data into a DB

        # check if the user is inside the criteria we want to follow/interact

        if (
            user.follower_count > Settings.get_action_config()["follower_min_count"]
            and user.following_count
            < Settings.get_action_config()["following_max_count"]
            and user.post_count > Settings.get_action_config()["min_post_count"]
        ):

            # follow and/or interact
            if (
                not self.session.is_followed()
                and Settings.get_action_config()["follow"]
            ):
                if (
                    random.randint(0, 100)
                    <= Settings.get_action_config()["follow_percent"]
                ):
                    if self.session.follow_user():
                        Logger.loginfo(
                            "User {} followed successfully".format(user.username)
                        )
                        self.followed += 1
                    else:
                        Logger.logerror(
                            "User {} was not followed".format(user.username)
                        )

            if self.session.is_followed() and Settings.get_action_config()["unfollow"]:
                if self.session.unfollow_user():
                    Logger.loginfo(
                        "User {} was unfollowed successfully".format(user.username)
                    )
                    self.unfollowed += 1
                else:
                    Logger.logerror("User {} was not unfollowed".format(user.username))

            if Settings.get_action_config()["user_interact"]:
                if (
                    random.randint(0, 100)
                    <= Settings.get_action_config()["user_interact_percent"]
                ):
                    # let's put ourselves in the feed mode by clicking a post
                    self.session.go_feed()
                    # transition to the feed state
                    self.go_feed()

    def on_enter_feed(self):
        """
        execute actions on a feed: browse through it, like, comment, follow
        :return:
        """

    def on_enter_idle(self):
        """
        execute the actions needed to go to the next actions
        ideally we randomize the states we want to go in and we trigger them
        :return:
        """
        # here we should have in the state machine only the states we can do
        # because we have data, otherwise the only state that it can go is in idle
        next_transition = "go_" + random.sample(self.states, 1)
        self.machine.trigger(next_transition)

        # we arrive at a permanent state of the FSM, we stay idle forever
