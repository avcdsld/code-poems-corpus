def sign(user=None,
         keyid=None,
         text=None,
         filename=None,
         output=None,
         use_passphrase=False,
         gnupghome=None):
    '''
    Sign message or file

    user
        Which user's keychain to access, defaults to user Salt is running as.
        Passing the user as ``salt`` will set the GnuPG home directory to the
        ``/etc/salt/gpgkeys``.

    keyid
        The keyid of the key to set the trust level for, defaults to
        first key in the secret keyring.

    text
        The text to sign.

    filename
        The filename to sign.

    output
        The filename where the signed file will be written, default is standard out.

    use_passphrase
        Whether to use a passphrase with the signing key. Passphrase is received
        from Pillar.

    gnupghome
        Specify the location where GPG keyring and related files are stored.

    CLI Example:

    .. code-block:: bash

        salt '*' gpg.sign text='Hello there.  How are you?'

        salt '*' gpg.sign filename='/path/to/important.file'

        salt '*' gpg.sign filename='/path/to/important.file' use_passphrase=True

    '''
    gpg = _create_gpg(user, gnupghome)
    if use_passphrase:
        gpg_passphrase = __salt__['pillar.get']('gpg_passphrase')
        if not gpg_passphrase:
            raise SaltInvocationError('gpg_passphrase not available in pillar.')
    else:
        gpg_passphrase = None

    # Check for at least one secret key to sign with

    gnupg_version = _LooseVersion(gnupg.__version__)
    if text:
        if gnupg_version >= '1.3.1':
            signed_data = gpg.sign(text, default_key=keyid, passphrase=gpg_passphrase)
        else:
            signed_data = gpg.sign(text, keyid=keyid, passphrase=gpg_passphrase)
    elif filename:
        with salt.utils.files.flopen(filename, 'rb') as _fp:
            if gnupg_version >= '1.3.1':
                signed_data = gpg.sign(text, default_key=keyid, passphrase=gpg_passphrase)
            else:
                signed_data = gpg.sign_file(_fp, keyid=keyid, passphrase=gpg_passphrase)
        if output:
            with salt.utils.files.flopen(output, 'w') as fout:
                fout.write(signed_data.data)
    else:
        raise SaltInvocationError('filename or text must be passed.')
    return signed_data.data