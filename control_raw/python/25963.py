def get_rsa_pub_key(path):
    '''
    Read a public key off the disk.
    '''
    log.debug('salt.crypt.get_rsa_pub_key: Loading public key')
    if HAS_M2:
        with salt.utils.files.fopen(path, 'rb') as f:
            data = f.read().replace(b'RSA ', b'')
        bio = BIO.MemoryBuffer(data)
        key = RSA.load_pub_key_bio(bio)
    else:
        with salt.utils.files.fopen(path) as f:
            key = RSA.importKey(f.read())
    return key