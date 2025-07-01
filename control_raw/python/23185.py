def delete_replication(Bucket,
           region=None, key=None, keyid=None, profile=None):
    '''
    Delete the replication config from the given bucket

    Returns {deleted: true} if replication configuration was deleted and returns
    {deleted: False} if replication configuration was not deleted.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_s3_bucket.delete_replication my_bucket

    '''

    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        conn.delete_bucket_replication(Bucket=Bucket)
        return {'deleted': True, 'name': Bucket}
    except ClientError as e:
        return {'deleted': False, 'error': __utils__['boto3.get_error'](e)}