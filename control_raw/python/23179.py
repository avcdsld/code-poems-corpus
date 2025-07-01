def put_request_payment(Bucket, Payer,
           region=None, key=None, keyid=None, profile=None):
    '''
    Given a valid config, update the request payment configuration for a bucket.

    Returns {updated: true} if request payment configuration was updated and returns
    {updated: False} if request payment configuration was not updated.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_s3_bucket.put_request_payment my_bucket Requester

    '''

    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        conn.put_bucket_request_payment(Bucket=Bucket, RequestPaymentConfiguration={
                'Payer': Payer,
        })
        return {'updated': True, 'name': Bucket}
    except ClientError as e:
        return {'updated': False, 'error': __utils__['boto3.get_error'](e)}