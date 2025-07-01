def set_reboot_required_witnessed():
    r'''
    This function is used to remember that an event indicating that a reboot is
    required was witnessed. This function relies on the salt-minion's ability to
    create the following volatile registry key in the *HKLM* hive:

       *SYSTEM\\CurrentControlSet\\Services\\salt-minion\\Volatile-Data*

    Because this registry key is volatile, it will not persist beyond the
    current boot session. Also, in the scope of this key, the name *'Reboot
    required'* will be assigned the value of *1*.

    For the time being, this function is being used whenever an install
    completes with exit code 3010 and can be extended where appropriate in the
    future.

    .. versionadded:: 2016.11.0

    Returns:
        bool: ``True`` if successful, otherwise ``False``

    CLI Example:

    .. code-block:: bash

        salt '*' system.set_reboot_required_witnessed
    '''
    return __utils__['reg.set_value'](
        hive='HKLM',
        key=MINION_VOLATILE_KEY,
        volatile=True,
        vname=REBOOT_REQUIRED_NAME,
        vdata=1,
        vtype='REG_DWORD')