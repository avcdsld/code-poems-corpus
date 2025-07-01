def _get_oath2_access_token(client_key, client_secret):
    '''
    Query the vistara API and get an access_token

    '''
    if not client_key and not client_secret:
        log.error(
            "client_key and client_secret have not been specified "
            "and are required parameters."
        )
        return False

    method = 'POST'
    url = 'https://api.vistara.io/auth/oauth/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    params = {
        'grant_type': 'client_credentials',
        'client_id': client_key,
        'client_secret': client_secret
    }

    resp = salt.utils.http.query(
        url=url,
        method=method,
        header_dict=headers,
        params=params,
        opts=__opts__
    )

    respbody = resp.get('body', None)

    if not respbody:
        return False

    access_token = salt.utils.json.loads(respbody)['access_token']
    return access_token