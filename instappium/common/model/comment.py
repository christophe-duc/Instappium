#!/usr/bin/env python3
"""
Comment model for interactions comment attributes and perform action on comments
"""


class Comment:
    def __init__(
        self,
        username=None,
        text=None,
        timestamp=None,
        like_count=None,
        reply_count=None,
    ):

        self._username = username
        self._text = text
        self._timestamp = timestamp

        self._like_count = like_count
        self._reply_count = reply_count

    # Used for working with sets
    def __hash__(self):
        return hash(self.username + self.text + self.timestamp)

    # Used for working with sets
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return hash(self) == hash(other)
        else:
            return False

    def __repr__(self):
        return "Comment({0}, {1}, {2}, {3}, {4}, {5})".format(
            hash(self),
            self.username,
            self.text,
            self.timestamp,
            self.like_count,
            self.reply_count,
        )

    def __str__(self):
        return repr(self)

    @property
    def username(self):
        """
        getter for User object representing the User who made the comment
        :return: User
        """
        return self._username

    @property
    def text(self):
        """
        getter for comment text
        :return:
        """

        return self._text

    @property
    def timestamp(self):
        """
        getter for timestamp of comment
        :return:
        """

        return self._timestamp

    @property
    def like_count(self):
        """
        getter for the amount of likes on the comment
        :return:
        """

        return self._like_count

    @property
    def reply_count(self):
        """
        getter for the amount of replies on the comment
        :return:
        """

        return self._reply_count
