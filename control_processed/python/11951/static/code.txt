def has_any_role(*items):
    r"""A :func:`.check` that is added that checks if the member invoking the
    command has **any** of the roles specified. This means that if they have
    one out of the three roles specified, then this check will return `True`.

    Similar to :func:`.has_role`\, the names or IDs passed in must be exact.

    This check raises one of two special exceptions, :exc:`.MissingAnyRole` if the user
    is missing all roles, or :exc:`.NoPrivateMessage` if it is used in a private message.
    Both inherit from :exc:`.CheckFailure`.

    .. versionchanged:: 1.1.0

        Raise :exc:`.MissingAnyRole` or :exc:`.NoPrivateMessage`
        instead of generic :exc:`.CheckFailure`

    Parameters
    -----------
    items: List[Union[:class:`str`, :class:`int`]]
        An argument list of names or IDs to check that the member has roles wise.

    Example
    --------

    .. code-block:: python3

        @bot.command()
        @commands.has_any_role('Library Devs', 'Moderators', 492212595072434186)
        async def cool(ctx):
            await ctx.send('You are cool indeed')
    """
    def predicate(ctx):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            raise NoPrivateMessage()

        getter = functools.partial(discord.utils.get, ctx.author.roles)
        if any(getter(id=item) is not None if isinstance(item, int) else getter(name=item) is not None for item in items):
            return True
        raise MissingAnyRole(items)

    return check(predicate)