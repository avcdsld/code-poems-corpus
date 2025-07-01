def get_progress(opts, out, progress):
    '''
    Get the progress bar from the given outputter
    '''
    return salt.loader.raw_mod(opts,
                                out,
                                'rawmodule',
                                mod='output')['{0}.progress_iter'.format(out)](progress)