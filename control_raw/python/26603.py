def list_certs(keychain="/Library/Keychains/System.keychain"):
    '''
    List all of the installed certificates

    keychain
        The keychain to install the certificate to, this defaults to
        /Library/Keychains/System.keychain

    CLI Example:

    .. code-block:: bash

        salt '*' keychain.list_certs
    '''
    cmd = 'security find-certificate -a {0} | grep -o "alis".*\\" | ' \
          'grep -o \'\\"[-A-Za-z0-9.:() ]*\\"\''.format(_quote(keychain))
    out = __salt__['cmd.run'](cmd, python_shell=True)
    return out.replace('"', '').split('\n')