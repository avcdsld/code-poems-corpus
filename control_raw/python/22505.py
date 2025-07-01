def describe_pipelines(pipeline_ids, region=None, key=None, keyid=None, profile=None):
    '''
    Retrieve metadata about one or more pipelines.

    CLI example:

    .. code-block:: bash

        salt myminion boto_datapipeline.describe_pipelines ['my_pipeline_id']
    '''
    client = _get_client(region, key, keyid, profile)
    r = {}
    try:
        r['result'] = client.describe_pipelines(pipelineIds=pipeline_ids)
    except (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError) as e:
        r['error'] = six.text_type(e)
    return r