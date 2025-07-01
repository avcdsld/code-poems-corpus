def refresh_grains(**kwargs):
    '''
    .. versionadded:: 2016.3.6,2016.11.4,2017.7.0

    Refresh the minion's grains without syncing custom grains modules from
    ``salt://_grains``.

    .. note::
        The available execution modules will be reloaded as part of this
        proceess, as grains can affect which modules are available.

    refresh_pillar : True
        Set to ``False`` to keep pillar data from being refreshed.

    CLI Examples:

    .. code-block:: bash

        salt '*' saltutil.refresh_grains
    '''
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    _refresh_pillar = kwargs.pop('refresh_pillar', True)
    if kwargs:
        salt.utils.args.invalid_kwargs(kwargs)
    # Modules and pillar need to be refreshed in case grains changes affected
    # them, and the module refresh process reloads the grains and assigns the
    # newly-reloaded grains to each execution module's __grains__ dunder.
    refresh_modules()
    if _refresh_pillar:
        refresh_pillar()
    return True