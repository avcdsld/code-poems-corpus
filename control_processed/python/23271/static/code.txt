def add_remote(name, location):
    '''
    Adds a new location to install flatpak packages from.

    Args:
        name (str): The repository's name.
        location (str): The location of the repository.

    Returns:
        dict: The ``result`` and ``output``.

    Example:

    .. code-block:: yaml

        add_flathub:
          flatpack.add_remote:
            - name: flathub
            - location: https://flathub.org/repo/flathub.flatpakrepo
    '''
    ret = {'name': name,
           'changes': {},
           'result': None,
           'comment': ''}

    old = __salt__['flatpak.is_remote_added'](name)
    if not old:
        if __opts__['test']:
            ret['comment'] = 'Remote "{0}" would have been added'.format(name)
            ret['changes']['new'] = name
            ret['changes']['old'] = None
            ret['result'] = None
            return ret

        install_ret = __salt__['flatpak.add_remote'](name)
        if __salt__['flatpak.is_remote_added'](name):
            ret['comment'] = 'Remote "{0}" was added'.format(name)
            ret['changes']['new'] = name
            ret['changes']['old'] = None
            ret['result'] = True
            return ret

        ret['comment'] = 'Failed to add remote "{0}"'.format(name)
        ret['comment'] += '\noutput:\n' + install_ret['output']
        ret['result'] = False
        return ret

    ret['comment'] = 'Remote "{0}" already exists'.format(name)
    if __opts__['test']:
        ret['result'] = None
        return ret

    ret['result'] = True
    return ret