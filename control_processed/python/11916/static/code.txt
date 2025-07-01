def overwrites_for(self, obj):
        """Returns the channel-specific overwrites for a member or a role.

        Parameters
        -----------
        obj
            The :class:`Role` or :class:`abc.User` denoting
            whose overwrite to get.

        Returns
        ---------
        :class:`PermissionOverwrite`
            The permission overwrites for this object.
        """

        if isinstance(obj, User):
            predicate = lambda p: p.type == 'member'
        elif isinstance(obj, Role):
            predicate = lambda p: p.type == 'role'
        else:
            predicate = lambda p: True

        for overwrite in filter(predicate, self._overwrites):
            if overwrite.id == obj.id:
                allow = Permissions(overwrite.allow)
                deny = Permissions(overwrite.deny)
                return PermissionOverwrite.from_pair(allow, deny)

        return PermissionOverwrite()