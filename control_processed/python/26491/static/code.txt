def _write_conf(conf, path=MAIN_CF):
    '''
    Write out configuration file.
    '''
    with salt.utils.files.fopen(path, 'w') as fh_:
        for line in conf:
            line = salt.utils.stringutils.to_str(line)
            if isinstance(line, dict):
                fh_.write(' '.join(line))
            else:
                fh_.write(line)
            fh_.write('\n')