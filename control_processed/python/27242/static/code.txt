def update_endtime(jid, time):
    '''
    Update (or store) the end time for a given job

    Endtime is stored as a plain text string
    '''
    jid_dir = salt.utils.jid.jid_dir(jid, _job_dir(), __opts__['hash_type'])
    try:
        if not os.path.exists(jid_dir):
            os.makedirs(jid_dir)
        with salt.utils.files.fopen(os.path.join(jid_dir, ENDTIME), 'w') as etfile:
            etfile.write(salt.utils.stringutils.to_str(time))
    except IOError as exc:
        log.warning('Could not write job invocation cache file: %s', exc)