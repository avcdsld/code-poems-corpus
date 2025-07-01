def getconfig():
    '''
    Return the selinux mode from the config file

    CLI Example:

    .. code-block:: bash

        salt '*' selinux.getconfig
    '''
    try:
        config = '/etc/selinux/config'
        with salt.utils.files.fopen(config, 'r') as _fp:
            for line in _fp:
                line = salt.utils.stringutils.to_unicode(line)
                if line.strip().startswith('SELINUX='):
                    return line.split('=')[1].capitalize().strip()
    except (IOError, OSError, AttributeError):
        return None
    return None