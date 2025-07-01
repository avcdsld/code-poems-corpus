def rpc(command, **kwargs):
    '''
    .. versionadded:: 2019.2.0

    This is a wrapper to execute RPC requests on various network operating
    systems supported by NAPALM, invoking the following functions for the NAPALM
    native drivers:

    - :py:func:`napalm.junos_rpc <salt.modules.napalm_mod.junos_rpc>` for ``junos``
    - :py:func:`napalm.pyeapi_run_commands <salt.modules.napalm_mod.pyeapi_run_commands>`
      for ``eos``
    - :py:func:`napalm.nxos_api_rpc <salt.modules.napalm_mod.nxos_api_rpc>` for
      ``nxos``
    - :py:func:`napalm.netmiko_commands <salt.modules.napalm_mod.netmiko_commands>`
      for ``ios``, ``iosxr``, and ``nxos_ssh``

    command
        The RPC command to execute. This depends on the nature of the operating
        system.

    kwargs
        Key-value arguments to be sent to the underlying Execution function.

    The function capabilities are extensible in the user environment via the
    ``napalm_rpc_map`` configuration option / Pillar, e.g.,

    .. code-block:: yaml

        napalm_rpc_map:
          f5: napalm.netmiko_commands
          panos: panos.call

    The mapping above reads: when the NAPALM ``os`` Grain is ``f5``, then call
    ``napalm.netmiko_commands`` for RPC requests.

    By default, if the user does not specify any map, non-native NAPALM drivers
    will invoke the ``napalm.netmiko_commands`` Execution function.

    CLI Example:

    .. code-block:: bash

        salt '*' napalm.rpc 'show version'
        salt '*' napalm.rpc get-interfaces
    '''
    default_map = {
        'junos': 'napalm.junos_rpc',
        'eos': 'napalm.pyeapi_run_commands',
        'nxos': 'napalm.nxos_api_rpc'
    }
    napalm_map = __salt__['config.get']('napalm_rpc_map', {})
    napalm_map.update(default_map)
    fun = napalm_map.get(__grains__['os'], 'napalm.netmiko_commands')
    return __salt__[fun](command, **kwargs)