def parse_csr():
    """
    Parse certificate signing request for domains
    """
    LOGGER.info("Parsing CSR...")
    cmd = [
        'openssl', 'req',
        '-in', os.path.join(gettempdir(), 'domain.csr'),
        '-noout',
        '-text'
    ]
    devnull = open(os.devnull, 'wb')
    out = subprocess.check_output(cmd, stderr=devnull)
    domains = set([])
    common_name = re.search(r"Subject:.*? CN\s?=\s?([^\s,;/]+)", out.decode('utf8'))
    if common_name is not None:
        domains.add(common_name.group(1))
    subject_alt_names = re.search(r"X509v3 Subject Alternative Name: \n +([^\n]+)\n", out.decode('utf8'), re.MULTILINE | re.DOTALL)
    if subject_alt_names is not None:
        for san in subject_alt_names.group(1).split(", "):
            if san.startswith("DNS:"):
                domains.add(san[4:])

    return domains