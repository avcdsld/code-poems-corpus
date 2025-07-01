def _file_write(path, content):
    '''
    Write content to a file
    '''
    with salt.utils.files.fopen(path, 'w+') as fp_:
        fp_.write(salt.utils.stringutils.to_str(content))
    fp_.close()