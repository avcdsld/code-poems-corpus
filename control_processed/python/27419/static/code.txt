def beacon(config):
    '''
    Check if installed packages are the latest versions
    and fire an event for those that have upgrades.

    .. code-block:: yaml

        beacons:
          pkg:
            - pkgs:
                - zsh
                - apache2
            - refresh: True
    '''
    ret = []

    _refresh = False
    pkgs = []
    for config_item in config:
        if 'pkgs' in config_item:
            pkgs += config_item['pkgs']
        if 'refresh' in config and config['refresh']:
            _refresh = True

    for pkg in pkgs:
        _installed = __salt__['pkg.version'](pkg)
        _latest = __salt__['pkg.latest_version'](pkg, refresh=_refresh)
        if _installed and _latest:
            _pkg = {'pkg': pkg,
                    'version': _latest
                    }
            ret.append(_pkg)
    return ret