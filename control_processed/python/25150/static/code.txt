def exists(name, tags=None, region=None, key=None, keyid=None, profile=None):
    '''
    Check to see if an RDS exists.

    CLI example::

        salt myminion boto_rds.exists myrds region=us-east-1
    '''
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)

    try:
        rds = conn.describe_db_instances(DBInstanceIdentifier=name)
        return {'exists': bool(rds)}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}