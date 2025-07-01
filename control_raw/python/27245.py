def load_reg():
    '''
    Load the register from msgpack files
    '''
    reg_dir = _reg_dir()
    regfile = os.path.join(reg_dir, 'register')
    try:
        with salt.utils.files.fopen(regfile, 'r') as fh_:
            return salt.utils.msgpack.load(fh_)
    except Exception:
        log.error('Could not write to msgpack file %s', __opts__['outdir'])
        raise