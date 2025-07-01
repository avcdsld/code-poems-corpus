def save_load(jid, load, minions=None):
    '''
    Save the load to the specified jid id
    '''
    # Load is being stored as a text datatype. Single quotes are used in the
    # VALUES list. Therefore, all single quotes contained in the results from
    # salt.utils.json.dumps(load) must be escaped Cassandra style.
    query = '''INSERT INTO {keyspace}.jids (
                 jid, load
               ) VALUES (?, ?)'''.format(keyspace=_get_keyspace())

    statement_arguments = [
        jid,
        salt.utils.json.dumps(load).replace("'", "''")
    ]

    # cassandra_cql.cql_query may raise a CommandExecutionError
    try:
        __salt__['cassandra_cql.cql_query_with_prepare'](query, 'save_load',
                                                         statement_arguments,
                                                         asynchronous=True)
    except CommandExecutionError:
        log.critical('Could not save load in jids table.')
        raise
    except Exception as e:
        log.critical('Unexpected error while inserting into jids: %s', e)
        raise