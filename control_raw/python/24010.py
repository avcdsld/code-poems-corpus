def option_present(name, value, reload=False):
    '''
    Ensure the state of a particular option/setting in csf.

    name
        The option name in csf.conf

    value
        The value it should be set to.

    reload
        Boolean. If set to true, csf will be reloaded after.
    '''
    ret = {'name': 'testing mode',
           'changes': {},
           'result': True,
           'comment': 'Option already present.'}
    option = name
    current_option = __salt__['csf.get_option'](option)
    if current_option:
        l = __salt__['csf.split_option'](current_option)
        option_value = l[1]
        if '"{0}"'.format(value) == option_value:
            return ret
        else:
            result = __salt__['csf.set_option'](option, value)
            ret['comment'] = 'Option modified.'
            ret['changes']['Option'] = 'Changed'
    else:
        result = __salt__['file.append']('/etc/csf/csf.conf',
                                            args='{0} = "{1}"'.format(option, value))
        ret['comment'] = 'Option not present. Appended to csf.conf'
        ret['changes']['Option'] = 'Changed.'
    if reload:
        if __salt__['csf.reload']():
            ret['comment'] += '. Csf reloaded.'
        else:
            ret['comment'] += '. Csf failed to reload.'
            ret['result'] = False
    return ret