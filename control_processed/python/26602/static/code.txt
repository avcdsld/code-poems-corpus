def uninstall(cert_name,
              keychain="/Library/Keychains/System.keychain",
              keychain_password=None):
    '''
    Uninstall a certificate from a keychain

    cert_name
        The name of the certificate to remove

    keychain
        The keychain to install the certificate to, this defaults to
        /Library/Keychains/System.keychain

    keychain_password
        If your keychain is likely to be locked pass the password and it will be unlocked
        before running the import

        Note: The password given here will show up as plaintext in the returned job
        info.

    CLI Example:

    .. code-block:: bash

        salt '*' keychain.install test.p12 test123
    '''
    if keychain_password is not None:
        unlock_keychain(keychain, keychain_password)

    cmd = 'security delete-certificate -c "{0}" {1}'.format(cert_name, keychain)
    return __salt__['cmd.run'](cmd)