def _find_file_meta(metadata, bucket_name, saltenv, path):
    '''
    Looks for a file's metadata in the S3 bucket cache file
    '''
    env_meta = metadata[saltenv] if saltenv in metadata else {}
    bucket_meta = {}
    for bucket in env_meta:
        if bucket_name in bucket:
            bucket_meta = bucket[bucket_name]
    files_meta = list(list(filter((lambda k: 'Key' in k), bucket_meta)))

    for item_meta in files_meta:
        if 'Key' in item_meta and item_meta['Key'] == path:
            try:
                # Get rid of quotes surrounding md5
                item_meta['ETag'] = item_meta['ETag'].strip('"')
            except KeyError:
                pass
            return item_meta