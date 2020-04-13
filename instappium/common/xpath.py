"""
class to store a relation between keywords and xpath in the UI
"""

class xpath:

    __xpath = {}

    __xpath["login"] = {
        "login_button": "//android.widget.TextView[@text='Log In']",
        "login_username": "//android.widget.EditText[@resource-id='com.instagram.android:id/login_username']",
        "login_password": "//android.widget.EditText[@resource-id='com.instagram.android:id/password']",
        "log_me_in_button": "//android.widget.TextView[@resource-id='com.instagram.android:id/button_text']",
    }

    __xpath["action_bar"] = {
        "home": "//android.widget.FrameLayout[@content-desc='Home' and @index=0]",
        "search": "//android.widget.FrameLayout[@content-desc='Search and Explore' and @index=1]",
        "camera": "//android.widget.FrameLayout[@content-desc='Camera' and @index=2]",
        "activity": "//android.widget.FrameLayout[@content-desc='Activity' and @index=3]",
        "profile": "//android.widget.FrameLayout[@content-desc='Profile' and @index=4]",

    }

    __xpath["search"] = {
        "search_text": "com.instagram.android:id/action_bar_search_edit_text",
        "search_user_results": "//android.widget.TextView[@resource-id='com.instagram.android:id/row_search_user_username']",
    }

    __xpath["profile"] = {
        "posts": "com.instagram.android:id/row_profile_header_textview_post_count",
        "followers": "com.instagram.android:id/row_profile_header_textview_followers_count",
        "following": "com.instagram.android:id/row_profile_header_textview_following_count"
    }

    @classmethod
    def read_xpath(cls, function_name, xpath_name):
        return cls.__xpath[function_name][xpath_name]