def update(table_name, throughput=None, global_indexes=None,
           region=None, key=None, keyid=None, profile=None):
    '''
    Update a DynamoDB table.

    CLI example::

        salt myminion boto_dynamodb.update table_name region=us-east-1
    '''
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    table = Table(table_name, connection=conn)
    return table.update(throughput=throughput, global_indexes=global_indexes)