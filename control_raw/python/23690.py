def _get_snapshot(name, suffix, blade):
    '''
    Return name of Snapshot
    or None
    '''
    try:
        filt = 'source=\'{}\' and suffix=\'{}\''.format(name, suffix)
        res = blade.file_system_snapshots.list_file_system_snapshots(filter=filt)
        return res.items[0]
    except rest.ApiException:
        return None