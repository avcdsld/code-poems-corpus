def get_name(principal):
    '''
    Gets the name from the specified principal.

    Args:

        principal (str):
            Find the Normalized name based on this. Can be a PySID object, a SID
            string, or a user name in any capitalization.

            .. note::
                Searching based on the user name can be slow on hosts connected
                to large Active Directory domains.

    Returns:
        str: The name that corresponds to the passed principal

    Usage:

    .. code-block:: python

        salt.utils.win_dacl.get_name('S-1-5-32-544')
        salt.utils.win_dacl.get_name('adminisTrators')
    '''
    # If this is a PySID object, use it
    if isinstance(principal, pywintypes.SIDType):
        sid_obj = principal
    else:
        # If None is passed, use the Universal Well-known SID for "Null SID"
        if principal is None:
            principal = 'S-1-0-0'
        # Try Converting String SID to SID Object first as it's least expensive
        try:
            sid_obj = win32security.ConvertStringSidToSid(principal)
        except pywintypes.error:
            # Try Getting the SID Object by Name Lookup last
            # This is expensive, especially on large AD Domains
            try:
                sid_obj = win32security.LookupAccountName(None, principal)[0]
            except pywintypes.error:
                # This is not a PySID object, a SID String, or a valid Account
                # Name. Just pass it and let the LookupAccountSid function try
                # to resolve it
                sid_obj = principal

    # By now we should have a valid PySID object
    try:
        return win32security.LookupAccountSid(None, sid_obj)[0]
    except (pywintypes.error, TypeError) as exc:
        message = 'Error resolving "{0}"'.format(principal)
        if type(exc) == pywintypes.error:
            win_error = win32api.FormatMessage(exc.winerror).rstrip('\n')
            message = '{0}: {1}'.format(message, win_error)
        log.exception(message)
        raise CommandExecutionError(message, exc)