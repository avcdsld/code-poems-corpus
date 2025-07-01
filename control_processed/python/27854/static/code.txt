def get_org_details(organization_id):
    '''
    Return the details for an organization

    CLI Example:

    .. code-block:: bash

        salt-run digicert.get_org_details 34

    Returns a dictionary with the org details, or with 'error' and 'status' keys.
    '''

    qdata = salt.utils.http.query(
        '{0}/organization/{1}'.format(_base_url(), organization_id),
        method='GET',
        decode=True,
        decode_type='json',
        header_dict={
            'X-DC-DEVKEY': _api_key(),
            'Content-Type': 'application/json',
        },
    )
    return qdata