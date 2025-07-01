def enabled(name, runas=None):
    '''
    Ensure the RabbitMQ plugin is enabled.

    name
        The name of the plugin
    runas
        The user to run the rabbitmq-plugin command as
    '''

    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}

    try:
        plugin_enabled = __salt__['rabbitmq.plugin_is_enabled'](name, runas=runas)
    except CommandExecutionError as err:
        ret['result'] = False
        ret['comment'] = 'Error: {0}'.format(err)
        return ret

    if plugin_enabled:
        ret['comment'] = 'Plugin \'{0}\' is already enabled.'.format(name)
        return ret

    if not __opts__['test']:
        try:
            __salt__['rabbitmq.enable_plugin'](name, runas=runas)
        except CommandExecutionError as err:
            ret['result'] = False
            ret['comment'] = 'Error: {0}'.format(err)
            return ret
    ret['changes'].update({'old': '', 'new': name})

    if __opts__['test'] and ret['changes']:
        ret['result'] = None
        ret['comment'] = 'Plugin \'{0}\' is set to be enabled.'.format(name)
        return ret

    ret['comment'] = 'Plugin \'{0}\' was enabled.'.format(name)
    return ret