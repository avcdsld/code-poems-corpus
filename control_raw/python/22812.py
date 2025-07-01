def installed(name, source):
    '''
    Ensure an update is installed on the minion

    Args:

        name(str):
            Name of the Windows KB ("KB123456")

        source (str):
            Source of .msu file corresponding to the KB

    Example:

    .. code-block:: yaml

        KB123456:
          wusa.installed:
            - source: salt://kb123456.msu
    '''
    ret = {'name': name,
           'changes': {},
           'result': False,
           'comment': ''}

    # Input validation
    if not name:
        raise SaltInvocationError('Must specify a KB "name"')
    if not source:
        raise SaltInvocationError('Must specify a "source" file to install')

    # Is the KB already installed
    if __salt__['wusa.is_installed'](name):
        ret['result'] = True
        ret['comment'] = '{0} already installed'.format(name)
        return ret

    # Check for test=True
    if __opts__['test'] is True:
        ret['result'] = None
        ret['comment'] = '{0} would be installed'.format(name)
        ret['result'] = None
        return ret

    # Cache the file
    cached_source_path = __salt__['cp.cache_file'](path=source, saltenv=__env__)
    if not cached_source_path:
        msg = 'Unable to cache {0} from saltenv "{1}"'.format(
            salt.utils.url.redact_http_basic_auth(source), __env__)
        ret['comment'] = msg
        return ret

    # Install the KB
    __salt__['wusa.install'](cached_source_path)

    # Verify successful install
    if __salt__['wusa.is_installed'](name):
        ret['comment'] = '{0} was installed'.format(name)
        ret['changes'] = {'old': False, 'new': True}
        ret['result'] = True
    else:
        ret['comment'] = '{0} failed to install'.format(name)

    return ret