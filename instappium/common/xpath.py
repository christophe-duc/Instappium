"""
class to store a relation between keywords and xpath in the UI
"""

class xpath:

    __xpath = {}

    __xpath["login"] = {
        "login_button": "//android.widget.TextView[@text='Log In']",
        "login_username": "//android.widget.EditText[@resource-id='com.instagram.android:id/login_username']",
        "login_password": "//android.widget.EditText[@resource-id='com.instagram.android:id/password']",
        "log_me_in_button": "//android.widget.TextView[@resource-id='com.instagram.android:id/button_text']"
    }

    @classmethod
    def read_xpath(cls, function_name, xpath_name):
        return cls.__xpath[function_name][xpath_name]