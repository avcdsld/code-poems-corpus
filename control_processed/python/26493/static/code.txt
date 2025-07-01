def delete(queue_id):
    '''
    Delete message(s) from the mail queue

    CLI Example:

    .. code-block:: bash

        salt '*' postfix.delete 5C33CA0DEA

        salt '*' postfix.delete ALL

    '''

    ret = {'message': '',
           'result': True
           }

    if not queue_id:
        log.error('Require argument queue_id')

    if not queue_id == 'ALL':
        queue = show_queue()
        _message = None
        for item in queue:
            if item['queue_id'] == queue_id:
                _message = item

        if not _message:
            ret['message'] = 'No message in queue with ID {0}'.format(queue_id)
            ret['result'] = False
            return ret

    cmd = 'postsuper -d {0}'.format(queue_id)
    result = __salt__['cmd.run_all'](cmd)

    if result['retcode'] == 0:
        if queue_id == 'ALL':
            ret['message'] = 'Successfully removed all messages'
        else:
            ret['message'] = 'Successfully removed message with queue id {0}'.format(queue_id)
    else:
        if queue_id == 'ALL':
            ret['message'] = 'Unable to removed all messages'
        else:
            ret['message'] = 'Unable to remove message with queue id {0}: {1}'.format(queue_id, result['stderr'])
    return ret