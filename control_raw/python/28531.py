def fire_exception(exc, opts, job=None, node='minion'):
    '''
    Fire raw exception across the event bus
    '''
    if job is None:
        job = {}
    event = salt.utils.event.SaltEvent(node, opts=opts, listen=False)
    event.fire_event(pack_exception(exc), '_salt_error')