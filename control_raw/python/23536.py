def send_msg(name, recipient, profile):
    '''
    Send a message to an XMPP user

    .. code-block:: yaml

        server-warning-message:
          xmpp.send_msg:
            - name: 'This is a server warning message'
            - profile: my-xmpp-account
            - recipient: admins@xmpp.example.com/salt

    name
        The message to send to the XMPP user
    '''
    ret = {'name': name,
           'changes': {},
           'result': None,
           'comment': ''}
    if __opts__['test']:
        ret['comment'] = 'Need to send message to {0}: {1}'.format(
            recipient,
            name,
        )
        return ret
    __salt__['xmpp.send_msg_multi'](
        message=name,
        recipients=[recipient],
        profile=profile,
    )
    ret['result'] = True
    ret['comment'] = 'Sent message to {0}: {1}'.format(recipient, name)
    return ret