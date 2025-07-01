def sign_certificate():
    """
    Get the new certificate.
    Returns the signed bytes.

    """
    LOGGER.info("Signing certificate...")
    cmd = [
        'openssl', 'req',
        '-in', os.path.join(gettempdir(), 'domain.csr'),
        '-outform', 'DER'
    ]
    devnull = open(os.devnull, 'wb')
    csr_der = subprocess.check_output(cmd, stderr=devnull)
    code, result = _send_signed_request(DEFAULT_CA + "/acme/new-cert", {
        "resource": "new-cert",
        "csr": _b64(csr_der),
    })
    if code != 201:
        raise ValueError("Error signing certificate: {0} {1}".format(code, result))
    LOGGER.info("Certificate signed!")

    return result