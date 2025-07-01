def stopped(name=None,
            containers=None,
            shutdown_timeout=None,
            unpause=False,
            error_on_absent=True,
            **kwargs):
    '''
    Ensure that a container (or containers) is stopped

    name
        Name or ID of the container

    containers
        Run this state on more than one container at a time. The following two
        examples accomplish the same thing:

        .. code-block:: yaml

            stopped_containers:
              docker_container.stopped:
                - names:
                  - foo
                  - bar
                  - baz

        .. code-block:: yaml

            stopped_containers:
              docker_container.stopped:
                - containers:
                  - foo
                  - bar
                  - baz

        However, the second example will be a bit quicker since Salt will stop
        all specified containers in a single run, rather than executing the
        state separately on each image (as it would in the first example).

    shutdown_timeout
        Timeout for graceful shutdown of the container. If this timeout is
        exceeded, the container will be killed. If this value is not passed,
        then the container's configured ``stop_timeout`` will be observed. If
        ``stop_timeout`` was also unset on the container, then a timeout of 10
        seconds will be used.

    unpause : False
        Set to ``True`` to unpause any paused containers before stopping. If
        unset, then an error will be raised for any container that was paused.

    error_on_absent : True
        By default, this state will return an error if any of the specified
        containers are absent. Set this to ``False`` to suppress that error.
    '''
    ret = {'name': name,
           'changes': {},
           'result': False,
           'comment': ''}

    if not name and not containers:
        ret['comment'] = 'One of \'name\' and \'containers\' must be provided'
        return ret
    if containers is not None:
        if not isinstance(containers, list):
            ret['comment'] = 'containers must be a list'
            return ret
        targets = []
        for target in containers:
            if not isinstance(target, six.string_types):
                target = six.text_type(target)
            targets.append(target)
    elif name:
        if not isinstance(name, six.string_types):
            targets = [six.text_type(name)]
        else:
            targets = [name]

    containers = {}
    for target in targets:
        try:
            c_state = __salt__['docker.state'](target)
        except CommandExecutionError:
            containers.setdefault('absent', []).append(target)
        else:
            containers.setdefault(c_state, []).append(target)

    errors = []
    if error_on_absent and 'absent' in containers:
        errors.append(
            'The following container(s) are absent: {0}'.format(
                ', '.join(containers['absent'])
            )
        )

    if not unpause and 'paused' in containers:
        ret['result'] = False
        errors.append(
            'The following container(s) are paused: {0}'.format(
                ', '.join(containers['paused'])
            )
        )

    if errors:
        ret['result'] = False
        ret['comment'] = '. '.join(errors)
        return ret

    to_stop = containers.get('running', []) + containers.get('paused', [])

    if not to_stop:
        ret['result'] = True
        if len(targets) == 1:
            ret['comment'] = 'Container \'{0}\' is '.format(targets[0])
        else:
            ret['comment'] = 'All specified containers are '
        if 'absent' in containers:
            ret['comment'] += 'absent or '
        ret['comment'] += 'not running'
        return ret

    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = (
            'The following container(s) will be stopped: {0}'
            .format(', '.join(to_stop))
        )
        return ret

    stop_errors = []
    for target in to_stop:
        stop_kwargs = {'unpause': unpause}
        if shutdown_timeout:
            stop_kwargs['timeout'] = shutdown_timeout
        changes = __salt__['docker.stop'](target, **stop_kwargs)
        if changes['result'] is True:
            ret['changes'][target] = changes
        else:
            if 'comment' in changes:
                stop_errors.append(changes['comment'])
            else:
                stop_errors.append(
                    'Failed to stop container \'{0}\''.format(target)
                )

    if stop_errors:
        ret['comment'] = '; '.join(stop_errors)
        return ret

    ret['result'] = True
    ret['comment'] = (
        'The following container(s) were stopped: {0}'
        .format(', '.join(to_stop))
    )
    return ret