def _get_container_service(container):
    '''
    Get the azure block blob service for the container in question

    Try account_key, sas_token, and no auth in that order
    '''
    if 'account_key' in container:
        account = azure.storage.CloudStorageAccount(container['account_name'], account_key=container['account_key'])
    elif 'sas_token' in container:
        account = azure.storage.CloudStorageAccount(container['account_name'], sas_token=container['sas_token'])
    else:
        account = azure.storage.CloudStorageAccount(container['account_name'])
    blob_service = account.create_block_blob_service()
    return blob_service