def is_friend(self):
        """:class:`bool`: Checks if the user is your friend.

        .. note::

            This only applies to non-bot accounts.
        """
        r = self.relationship
        if r is None:
            return False
        return r.type is RelationshipType.friend