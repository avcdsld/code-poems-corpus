def maybe_fix_ssl_version(ca_name, cacert_path=None, ca_filename=None):
    '''
    Check that the X509 version is correct
    (was incorrectly set in previous salt versions).
    This will fix the version if needed.

    ca_name
        ca authority name
    cacert_path
        absolute path to ca certificates root directory
    ca_filename
        alternative filename for the CA

        .. versionadded:: 2015.5.3


    CLI Example:

    .. code-block:: bash

        salt '*' tls.maybe_fix_ssl_version test_ca /etc/certs
    '''
    set_ca_path(cacert_path)
    if not ca_filename:
        ca_filename = '{0}_ca_cert'.format(ca_name)
    certp = '{0}/{1}/{2}.crt'.format(
            cert_base_path(),
            ca_name,
            ca_filename)
    ca_keyp = '{0}/{1}/{2}.key'.format(
        cert_base_path(),
        ca_name,
        ca_filename)
    with salt.utils.files.fopen(certp) as fic:
        cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,
                                               fic.read())
        if cert.get_version() == 3:
            log.info('Regenerating wrong x509 version '
                     'for certificate %s', certp)
            with salt.utils.files.fopen(ca_keyp) as fic2:
                try:
                    # try to determine the key bits
                    key = OpenSSL.crypto.load_privatekey(
                        OpenSSL.crypto.FILETYPE_PEM, fic2.read())
                    bits = key.bits()
                except Exception:
                    bits = 2048
                try:
                    days = (datetime.strptime(
                        cert.get_notAfter(),
                        '%Y%m%d%H%M%SZ') - datetime.utcnow()).days
                except (ValueError, TypeError):
                    days = 365
                subj = cert.get_subject()
                create_ca(
                    ca_name,
                    bits=bits,
                    days=days,
                    CN=subj.CN,
                    C=subj.C,
                    ST=subj.ST,
                    L=subj.L,
                    O=subj.O,
                    OU=subj.OU,
                    emailAddress=subj.emailAddress,
                    fixmode=True)