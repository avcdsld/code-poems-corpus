def add(name, keystore, passphrase, certificate, private_key=None):
    '''
    Adds certificates to an existing keystore or creates a new one if necesssary.

    :param name: alias for the certificate
    :param keystore: The path to the keystore file to query
    :param passphrase: The passphrase to use to decode the keystore
    :param certificate: The PEM public certificate to add to keystore. Can be a string for file.
    :param private_key: (Optional for TrustedCert) The PEM private key to add to the keystore

    CLI Example:

    .. code-block:: bash

        salt '*' keystore.add aliasname /tmp/test.store changeit /tmp/testcert.crt
        salt '*' keystore.add aliasname /tmp/test.store changeit certificate="-----BEGIN CERTIFICATE-----SIb...BM=-----END CERTIFICATE-----"
        salt '*' keystore.add keyname /tmp/test.store changeit /tmp/512.cert private_key=/tmp/512.key

    '''
    ASN1 = OpenSSL.crypto.FILETYPE_ASN1
    PEM = OpenSSL.crypto.FILETYPE_PEM
    certs_list = []
    if os.path.isfile(keystore):
        keystore_object = jks.KeyStore.load(keystore, passphrase)
        for alias, loaded_cert in keystore_object.entries.items():
            certs_list.append(loaded_cert)

    try:
        cert_string = __salt__['x509.get_pem_entry'](certificate)
    except SaltInvocationError:
        raise SaltInvocationError('Invalid certificate file or string: {0}'.format(certificate))

    if private_key:
        # Accept PEM input format, but convert to DES for loading into new keystore
        key_string = __salt__['x509.get_pem_entry'](private_key)
        loaded_cert = OpenSSL.crypto.load_certificate(PEM, cert_string)
        loaded_key = OpenSSL.crypto.load_privatekey(PEM, key_string)
        dumped_cert = OpenSSL.crypto.dump_certificate(ASN1, loaded_cert)
        dumped_key = OpenSSL.crypto.dump_privatekey(ASN1, loaded_key)

        new_entry = jks.PrivateKeyEntry.new(name, [dumped_cert], dumped_key, 'rsa_raw')
    else:
        new_entry = jks.TrustedCertEntry.new(name, cert_string)

    certs_list.append(new_entry)

    keystore_object = jks.KeyStore.new('jks', certs_list)
    keystore_object.save(keystore, passphrase)
    return True