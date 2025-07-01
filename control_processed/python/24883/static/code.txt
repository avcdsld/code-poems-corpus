def container_setting(name, container, settings=None):
    '''
    Set the value of the setting for an IIS container.

    :param str name: The name of the IIS container.
    :param str container: The type of IIS container. The container types are:
        AppPools, Sites, SslBindings
    :param str settings: A dictionary of the setting names and their values.
        Example of usage for the ``AppPools`` container:

    .. code-block:: yaml

        site0-apppool-setting:
            win_iis.container_setting:
                - name: site0
                - container: AppPools
                - settings:
                    managedPipelineMode: Integrated
                    processModel.maxProcesses: 1
                    processModel.userName: TestUser
                    processModel.password: TestPassword
                    processModel.identityType: SpecificUser

    Example of usage for the ``Sites`` container:

    .. code-block:: yaml

        site0-site-setting:
            win_iis.container_setting:
                - name: site0
                - container: Sites
                - settings:
                    logFile.logFormat: W3C
                    logFile.period: Daily
                    limits.maxUrlSegments: 32
    '''

    identityType_map2string = {0: 'LocalSystem', 1: 'LocalService', 2: 'NetworkService', 3: 'SpecificUser', 4: 'ApplicationPoolIdentity'}
    ret = {'name': name,
           'changes': {},
           'comment': str(),
           'result': None}

    if not settings:
        ret['comment'] = 'No settings to change provided.'
        ret['result'] = True
        return ret

    ret_settings = {
        'changes': {},
        'failures': {},
    }

    current_settings = __salt__['win_iis.get_container_setting'](name=name,
                                                                 container=container,
                                                                 settings=settings.keys())
    for setting in settings:
        # map identity type from numeric to string for comparing
        if setting == 'processModel.identityType' and settings[setting] in identityType_map2string.keys():
            settings[setting] = identityType_map2string[settings[setting]]

        if str(settings[setting]) != str(current_settings[setting]):
            ret_settings['changes'][setting] = {'old': current_settings[setting],
                                                'new': settings[setting]}
    if not ret_settings['changes']:
        ret['comment'] = 'Settings already contain the provided values.'
        ret['result'] = True
        return ret
    elif __opts__['test']:
        ret['comment'] = 'Settings will be changed.'
        ret['changes'] = ret_settings
        return ret

    __salt__['win_iis.set_container_setting'](name=name, container=container, settings=settings)

    new_settings = __salt__['win_iis.get_container_setting'](name=name,
                                                             container=container,
                                                             settings=settings.keys())
    for setting in settings:
        if str(settings[setting]) != str(new_settings[setting]):
            ret_settings['failures'][setting] = {'old': current_settings[setting],
                                                 'new': new_settings[setting]}
            ret_settings['changes'].pop(setting, None)

    if ret_settings['failures']:
        ret['comment'] = 'Some settings failed to change.'
        ret['changes'] = ret_settings
        ret['result'] = False
    else:
        ret['comment'] = 'Set settings to contain the provided values.'
        ret['changes'] = ret_settings['changes']
        ret['result'] = True

    return ret