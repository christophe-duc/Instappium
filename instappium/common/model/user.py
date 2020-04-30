"""
User class: its intended as a class to ONLY store data about an user;
it performs no actions; if actions are needed, they will be performed
through the AppiumUserActions or SeleniumUserActions static class.
"""


class User:
    def __init__(
        self,
        username: str,
        post_count: int = None,
        follower_count: int = None,
        following_count: int = None,
        full_name: str = None,
        bio: str = None,
        category: str = None,
    ):
        """
        init
        """
        self.username = username
        self._post_count = post_count
        self._follower_count = follower_count
        self._following_count = following_count
        self._full_name = full_name
        self._bio = bio
        self._category = category

    # Used for working with sets
    def __hash__(self):
        return hash(self.username)

    # Used for working with sets
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return hash(self) == hash(other)
        else:
            return False

    def __repr__(self):
        return "User information: \n\thash (id): {}, \n\tusername: {}, \n\tpost count: {}, \n\tfollower count: {},\
            \n\tfollowing count: {}, \n\tfull name: {},\n\tbio: {}\n\tcategory: {}".format(
            hash(self),
            self.username,
            self.post_count,
            self.follower_count,
            self.following_count,
            self.full_name,
            self.bio,
            self.category,
        )

    def __str__(self):
        return repr(self)

    @property
    def post_count(self):
        """
        Getter for post_count (self.post_count will call this function automatically)
        :return:
        """
        return self._post_count

    @post_count.setter
    def post_count(self, amount):
        """
        Setter for post_count
        :param amount:
        :return:
        """
        self._post_count = amount

    @property
    def follower_count(self):
        """
        Getter for follower_count (self.follower_count will call this function automatically)
        :return:
        """
        return self._follower_count

    @follower_count.setter
    def follower_count(self, amount):
        self._follower_count = amount

    @property
    def following_count(self):
        """
        Getter for following_count (self.following_count will call this function automatically)
        :return:
        """
        return self._following_count

    @following_count.setter
    def following_count(self, amount):
        self._following_count = amount

    @property
    def bio(self):
        """
        Getter for the bio
        :return:
        """
        return self._bio

    @bio.setter
    def bio(self, text):
        self._bio = text

    @property
    def full_name(self):
        """
        Getter for the header description
        :return:
        """
        return self._full_name

    @full_name.setter
    def full_name(self, text):
        self._full_name = text

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, text):
        self._category = text
