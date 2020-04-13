"""
Class to define the Logger
"""

# import helpers
from .helper_functions import interruption_handler

# import libraries
from datetime import datetime
import logging
import logging.handlers
from math import ceil

# import drivers.actions


class Logger(object):
    """
    should contain all the function used throughout the code related to logging
    Class vars:
      -
    Instance vars:
      - __logfile
      - username
      - logfolder
      - show_logs
      - log_handler
    """

    def __init__(
        self,
        username: str = "",
        logfolder: str = "",
        show_logs: bool = False,
        log_handler=None,
    ):
        self.username = username
        self.logfolder = logfolder
        self.show_logs = show_logs

        self.__logfile = logging.getLogger(self.username)
        self.__logfile.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler("{}general.log".format(self.logfolder))
        file_handler.setLevel(logging.DEBUG)
        extra = {"username": self.username}
        logger_formatter = logging.Formatter(
            "%(levelname)s [%(asctime)s] [%(username)s]  %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(logger_formatter)
        self.__logfile.addHandler(file_handler)

        # add custom user handler if given
        if log_handler:
            self.__logfile.addHandler(log_handler)

        if self.show_logs is True:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(logger_formatter)
            self.__logfile.addHandler(console_handler)

        self.__logfile = logging.LoggerAdapter(self.__logfile, extra)

    @property
    def logfile(self):
        return self.__logfile

    def loginfo(self, message: str = ""):
        self.__logfile.info(message)

    def logerror(self, message: str = ""):
        self.__logfile.error(message)

    def logwarning(self, message: str = ""):
        self.__logfile.warning(message)

    def highlight_print(self, message=None, message_type=None, level=None):
        """ Print headers in a highlighted style """

        upper_char = ""
        lower_char = ""

        output_len = (
            28 + len(self.username) + 3 + len(message) if self.__logfile else len(message)
        )

        if message_type in ["initialization", "end"]:
            # OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
            # E.g.:          Session started!
            # oooooooooooooooooooooooooooooooooooooooooooooooo
            upper_char = "O"
            lower_char = "o"

        elif message_type == "login":
            # ................................................
            # E.g.:        Logged in successfully!
            # ''''''''''''''''''''''''''''''''''''''''''''''''
            upper_char = "."
            lower_char = "'"

        elif message_type == "feature":  # feature highlighter
            # ________________________________________________
            # E.g.:    Starting to interact by users..
            # """"""""""""""""""""""""""""""""""""""""""""""""
            upper_char = "_"
            lower_char = '"'

        elif message_type == "user iteration":
            # ::::::::::::::::::::::::::::::::::::::::::::::::
            # E.g.:            User: [1/4]
            upper_char = ":"
            lower_char = None

        elif message_type == "post iteration":
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # E.g.:            Post: [2/10]
            upper_char = "~"
            lower_char = None

        elif message_type == "workspace":
            # ._. ._. ._. ._. ._. ._. ._. ._. ._. ._. ._. ._.
            # E.g.: |> Workspace in use: "C:/Users/El/InstaPy"
            upper_char = " ._. "
            lower_char = None

        if upper_char and (self.show_logs or message_type == "workspace"):
            print("{}".format(upper_char * int(ceil(output_len / len(upper_char)))))

        if level == "info":
            if self.__logfile:
                self.loginfo(message)
            else:
                print(message)

        elif level == "warning":
            if self.__logfile:
                self.logwarning(message)
            else:
                print(message)

        if lower_char and (self.show_logs or message_type == "workspace"):
            print("{}".format(lower_char * int(ceil(output_len / len(lower_char)))))

    @staticmethod
    def get_log_time():
        """ this method will keep same format for all recored"""
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        return log_time

