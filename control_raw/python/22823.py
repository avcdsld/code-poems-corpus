def event_return(events):
    '''
    Return event to mysql server

    Requires that configuration be enabled via 'event_return'
    option in master config.
    '''
    with _get_serv(events, commit=True) as cur:
        for event in events:
            tag = event.get('tag', '')
            data = event.get('data', '')
            sql = '''INSERT INTO `salt_events` (`tag`, `data`, `master_id`)
                     VALUES (%s, %s, %s)'''
            cur.execute(sql, (tag, salt.utils.json.dumps(data), __opts__['id']))