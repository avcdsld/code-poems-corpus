def get_cert(zappa_instance, log=LOGGER, CA=DEFAULT_CA):
    """
    Call LE to get a new signed CA.
    """
    out = parse_account_key()
    header = get_boulder_header(out)
    accountkey_json = json.dumps(header['jwk'], sort_keys=True, separators=(',', ':'))
    thumbprint = _b64(hashlib.sha256(accountkey_json.encode('utf8')).digest())

    # find domains
    domains = parse_csr()

    # get the certificate domains and expiration
    register_account()

    # verify each domain
    for domain in domains:
        log.info("Verifying {0}...".format(domain))

        # get new challenge
        code, result = _send_signed_request(CA + "/acme/new-authz", {
            "resource": "new-authz",
            "identifier": {"type": "dns", "value": domain},
        })
        if code != 201:
            raise ValueError("Error requesting challenges: {0} {1}".format(code, result))

        challenge = [ch for ch in json.loads(result.decode('utf8'))['challenges'] if ch['type'] == "dns-01"][0]
        token = re.sub(r"[^A-Za-z0-9_\-]", "_", challenge['token'])
        keyauthorization = "{0}.{1}".format(token, thumbprint).encode('utf-8')

        # sha256_b64
        digest = _b64(hashlib.sha256(keyauthorization).digest())

        zone_id = zappa_instance.get_hosted_zone_id_for_domain(domain)
        if not zone_id:
            raise ValueError("Could not find Zone ID for: " + domain)
        zappa_instance.set_dns_challenge_txt(zone_id, domain, digest)  # resp is unused

        print("Waiting for DNS to propagate..")

        # What's optimal here?
        # import time  # double import; import in loop; shadowed import
        time.sleep(45)

        # notify challenge are met
        code, result = _send_signed_request(challenge['uri'], {
            "resource": "challenge",
            "keyAuthorization": keyauthorization.decode('utf-8'),
        })
        if code != 202:
            raise ValueError("Error triggering challenge: {0} {1}".format(code, result))

        # wait for challenge to be verified
        verify_challenge(challenge['uri'])

        # Challenge verified, clean up R53
        zappa_instance.remove_dns_challenge_txt(zone_id, domain, digest)

    # Sign
    result = sign_certificate()
    # Encode to PEM format
    encode_certificate(result)

    return True