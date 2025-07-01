async def set_permissions(self, target, *, overwrite=_undefined, reason=None, **permissions):
        r"""|coro|

        Sets the channel specific permission overwrites for a target in the
        channel.

        The ``target`` parameter should either be a :class:`Member` or a
        :class:`Role` that belongs to guild.

        The ``overwrite`` parameter, if given, must either be ``None`` or
        :class:`PermissionOverwrite`. For convenience, you can pass in
        keyword arguments denoting :class:`Permissions` attributes. If this is
        done, then you cannot mix the keyword arguments with the ``overwrite``
        parameter.

        If the ``overwrite`` parameter is ``None``, then the permission
        overwrites are deleted.

        You must have the :attr:`~Permissions.manage_roles` permission to use this.

        Examples
        ----------

        Setting allow and deny: ::

            await message.channel.set_permissions(message.author, read_messages=True,
                                                                  send_messages=False)

        Deleting overwrites ::

            await channel.set_permissions(member, overwrite=None)

        Using :class:`PermissionOverwrite` ::

            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = True
            await channel.set_permissions(member, overwrite=overwrite)

        Parameters
        -----------
        target
            The :class:`Member` or :class:`Role` to overwrite permissions for.
        overwrite: :class:`PermissionOverwrite`
            The permissions to allow and deny to the target.
        \*\*permissions
            A keyword argument list of permissions to set for ease of use.
            Cannot be mixed with ``overwrite``.
        reason: Optional[:class:`str`]
            The reason for doing this action. Shows up on the audit log.

        Raises
        -------
        Forbidden
            You do not have permissions to edit channel specific permissions.
        HTTPException
            Editing channel specific permissions failed.
        NotFound
            The role or member being edited is not part of the guild.
        InvalidArgument
            The overwrite parameter invalid or the target type was not
            :class:`Role` or :class:`Member`.
        """

        http = self._state.http

        if isinstance(target, User):
            perm_type = 'member'
        elif isinstance(target, Role):
            perm_type = 'role'
        else:
            raise InvalidArgument('target parameter must be either Member or Role')

        if isinstance(overwrite, _Undefined):
            if len(permissions) == 0:
                raise InvalidArgument('No overwrite provided.')
            try:
                overwrite = PermissionOverwrite(**permissions)
            except (ValueError, TypeError):
                raise InvalidArgument('Invalid permissions given to keyword arguments.')
        else:
            if len(permissions) > 0:
                raise InvalidArgument('Cannot mix overwrite and keyword arguments.')

        # TODO: wait for event

        if overwrite is None:
            await http.delete_channel_permissions(self.id, target.id, reason=reason)
        elif isinstance(overwrite, PermissionOverwrite):
            (allow, deny) = overwrite.pair()
            await http.edit_channel_permissions(self.id, target.id, allow.value, deny.value, perm_type, reason=reason)
        else:
            raise InvalidArgument('Invalid overwrite type provided.')