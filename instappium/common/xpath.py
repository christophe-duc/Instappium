"""
class to store a relation between keywords and xpath in the UI
"""

# we have to migrate out of xpath (as it is inefficient and use id


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
        "back": "com.instagram.android:id/action_bar_button_back",
    }

    __xpath["search"] = {
        "search_text": "com.instagram.android:id/action_bar_search_edit_text",
        "accounts": "//android.widget.TextView[@resource-id='com.instagram.android:id/tab_button_name_text' "
        "and @text='ACCOUNTS']",
        "hashtags": "//android.widget.TextView[@resource-id='com.instagram.android:id/tab_button_name_text' "
        "and @text='TAGS']",
        "places": "//android.widget.TextView[@resource-id='com.instagram.android:id/tab_button_name_text' "
        "and @text='PLACES']",
        "accounts_results": "com.instagram.android:id/row_search_user_username",
        "hashtags_results": "com.instagram.android:id/row_hashtag_textview_tag_name",
        "places_results": "com.instagram.android:id/row_place_title",
        "top": "//android.widget.TextView[@text='TOP']",
        "recent": "//android.widget.TextView[@text='RECENT']",
        "post_imagelist": "com.instagram.android:id/image_button",
        "post_videolist": "com.instagram.android:id/layout_container",
    }

    __xpath["profile"] = {
        "username": "com.instagram.android:id/title_view",
        "username_back": "com.instagram.android:id/action_bar_textview_title",
        "posts": "com.instagram.android:id/row_profile_header_textview_post_count",
        "followers": "com.instagram.android:id/row_profile_header_textview_followers_count",
        "following": "com.instagram.android:id/row_profile_header_textview_following_count",
        "fullname": "com.instagram.android:id/profile_header_full_name",
        "category": "com.instagram.android:id/profile_header_business_category",
        "website": "com.instagram.android:id/profile_header_website",
        "bio": "com.instagram.android:id/profile_header_bio_text",
        "following_button": "//android.widget.TextView[@text='Following']",
        "message_button": "//android.widget.TextView[@text='Message']",
        "similar_accounts": "com.instagram.android:id/row_profile_header_button_chaining",
        "featured_stories": "com.instagram.android:id/avatar_container",
        "grid_posts": "//android.widget.ImageView[@content-desc='Grid View']",
        "tagged_posts": "//android.widget.ImageView[@content-desc='Photos of You']",
        "content_row": "com.instagram.android:id/media_set_row_content_identifier",
    }

    __xpath["feed"] = {
        "username": "com.instagram.android:id/row_feed_photo_profile_name",
        "follow_button": "//android.widget.TextView[@text='Follow']",
        "like": "com.instagram.android:id/row_feed_button_like",
        "comment": "com.instagram.android:id/row_feed_button_comment",
        "share": "com.instagram.android:id/row_feed_button_share",
        "save": "com.instagram.android:id/row_feed_button_save",
    }

    @classmethod
    def read_xpath(cls, function_name, xpath_name):
        return cls.__xpath[function_name][xpath_name]
