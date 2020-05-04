"""
Where we keep all the stats of a session
"""

# libraries import
import time

from instappium.common.helper_functions import truncate_float


class Stats(object):
    """
    handling the stats of an instappium session
    """

    start_time = time.time()
    liked_img = 0
    already_liked = 0
    liked_comments = 0
    commented = 0
    replied_to_comments = 0
    followed = 0
    already_followed = 0
    unfollowed = 0
    followed_by = 0
    following_num = 0
    inap_img = 0
    not_valid_users = 0
    video_played = 0
    already_Visited = 0
    stories_watched = 0
    reels_watched = 0

    @classmethod
    def live_report(cls):
        """
           adapted version of instappium live report function for showing up on a telegram message
           :return:
           """
        stats = [
            cls.liked_img,
            cls.already_liked,
            cls.commented,
            cls.followed,
            cls.already_followed,
            cls.unfollowed,
            cls.stories_watched,
            cls.reels_watched,
            cls.inap_img,
            cls.not_valid_users,
        ]

        sessional_run_time = cls._run_time()
        run_time_info = (
            "{} seconds".format(sessional_run_time)
            if sessional_run_time < 60
            else "{} minutes".format(truncate_float(sessional_run_time / 60, 2))
            if sessional_run_time < 3600
            else "{} hours".format(truncate_float(sessional_run_time / 60 / 60, 2))
        )
        run_time_msg = "[Session lasted {}]".format(run_time_info)

        if any(stat for stat in stats):
            return (
                "Sessional Live Report:\n"
                "|> LIKED {} images\n"
                "|> ALREADY LIKED: {}\n"
                "|> COMMENTED on {} images\n"
                "|> FOLLOWED {} users\n"
                "|> ALREADY FOLLOWED: {}\n"
                "|> UNFOLLOWED {} users\n"
                "|> LIKED {} comments\n"
                "|> REPLIED to {} comments\n"
                "|> INAPPROPRIATE images: {}\n"
                "|> NOT VALID users: {}\n"
                "|> WATCHED {} story(ies)\n"
                "|> WATCHED {} reel(s)\n"
                "\n{}".format(
                    cls.liked_img,
                    cls.already_liked,
                    cls.commented,
                    cls.followed,
                    cls.already_followed,
                    cls.unfollowed,
                    cls.liked_comments,
                    cls.replied_to_comments,
                    cls.inap_img,
                    cls.not_valid_users,
                    cls.stories_watched,
                    cls.reels_watched,
                    run_time_msg,
                )
            )
        else:
            return (
                "Sessional Live Report:\n"
                "|> No any statistics to show\n"
                "\n{}".format(run_time_msg)
            )

    def _run_time(self):
        """
        get the time spent in the current session
        :return:
        """
        real_time = time.time()
        run_time = real_time - self.start_time
        run_time = truncate_float(run_time, 2)

        return run_time
