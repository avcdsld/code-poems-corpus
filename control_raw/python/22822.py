def returner(ret):
    '''
    Return data to a mysql server
    '''
    # if a minion is returning a standalone job, get a jobid
    if ret['jid'] == 'req':
        ret['jid'] = prep_jid(nocache=ret.get('nocache', False))
        save_load(ret['jid'], ret)

    try:
        with _get_serv(ret, commit=True) as cur:
            sql = '''INSERT INTO `salt_returns`
                     (`fun`, `jid`, `return`, `id`, `success`, `full_ret`)
                     VALUES (%s, %s, %s, %s, %s, %s)'''

            cur.execute(sql, (ret['fun'], ret['jid'],
                              salt.utils.json.dumps(ret['return']),
                              ret['id'],
                              ret.get('success', False),
                              salt.utils.json.dumps(ret)))
    except salt.exceptions.SaltMasterError as exc:
        log.critical(exc)
        log.critical('Could not store return with MySQL returner. MySQL server unavailable.')