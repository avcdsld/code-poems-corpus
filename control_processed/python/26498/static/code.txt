def remove(name, keystore, passphrase):
    '''
    Removes a certificate from an existing keystore.
    Returns True if remove was successful, otherwise False

    :param name: alias for the certificate
    :param keystore: The path to the keystore file to query
    :param passphrase: The passphrase to use to decode the keystore

    CLI Example:

    .. code-block:: bash

        salt '*' keystore.remove aliasname /tmp/test.store changeit
    '''
    certs_list = []
    keystore_object = jks.KeyStore.load(keystore, passphrase)
    for alias, loaded_cert in keystore_object.entries.items():
        if name not in alias:
            certs_list.append(loaded_cert)

    if len(keystore_object.entries) != len(certs_list):
        # Entry has been removed, save keystore updates
        keystore_object = jks.KeyStore.new('jks', certs_list)
        keystore_object.save(keystore, passphrase)
        return True
    else:
        # No alias found, notify user
        return False