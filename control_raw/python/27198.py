def ca_exists(ca_name, cacert_path=None, ca_filename=None):
    '''
    Verify whether a Certificate Authority (CA) already exists

    ca_name
        name of the CA
    cacert_path
        absolute path to ca certificates root directory
    ca_filename
        alternative filename for the CA

        .. versionadded:: 2015.5.3


    CLI Example:

    .. code-block:: bash

        salt '*' tls.ca_exists test_ca /etc/certs
    '''
    set_ca_path(cacert_path)
    if not ca_filename:
        ca_filename = '{0}_ca_cert'.format(ca_name)
    certp = '{0}/{1}/{2}.crt'.format(
            cert_base_path(),
            ca_name,
            ca_filename)
    if os.path.exists(certp):
        maybe_fix_ssl_version(ca_name,
                              cacert_path=cacert_path,
                              ca_filename=ca_filename)
        return True
    return False