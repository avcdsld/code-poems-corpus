def sshfp_data(key_t, hash_t, pub):
    '''
    Generate an SSHFP record
    :param key_t: rsa/dsa/ecdsa/ed25519
    :param hash_t: sha1/sha256
    :param pub: the SSH public key
    '''
    key_t = RFC.validate(key_t, RFC.SSHFP_ALGO, 'in')
    hash_t = RFC.validate(hash_t, RFC.SSHFP_HASH)

    hasher = hashlib.new(hash_t)
    hasher.update(
        base64.b64decode(pub)
    )
    ssh_fp = hasher.hexdigest()

    return _rec2data(key_t, hash_t, ssh_fp)