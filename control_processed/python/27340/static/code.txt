def update_global_secondary_index(table_name, global_indexes, region=None,
                                  key=None, keyid=None, profile=None):
    '''
    Updates the throughput of the given global secondary indexes.

    CLI Example:
    .. code-block:: bash

        salt myminion boto_dynamodb.update_global_secondary_index table_name /
        indexes
    '''
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    table = Table(table_name, connection=conn)
    return table.update_global_secondary_index(global_indexes)