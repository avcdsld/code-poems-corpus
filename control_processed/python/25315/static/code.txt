def assign_license(license_key, license_name, entity, entity_display_name,
                   safety_checks=True, service_instance=None):
    '''
    Assigns a license to an entity

    license_key
        Key of the license to assign
        See ``_get_entity`` docstrings for format.

    license_name
        Display name of license

    entity
        Dictionary representation of an entity

    entity_display_name
        Entity name used in logging

    safety_checks
        Specify whether to perform safety check or to skip the checks and try
        performing the required task. Default is False.

    service_instance
        Service instance (vim.ServiceInstance) of the vCenter/ESXi host.
        Default is None.

    .. code-block:: bash

        salt '*' vsphere.assign_license license_key=00000:00000
            license name=test entity={type:cluster,datacenter:dc,cluster:cl}
    '''
    log.trace('Assigning license %s to entity %s', license_key, entity)
    _validate_entity(entity)
    if safety_checks:
        licenses = salt.utils.vmware.get_licenses(service_instance)
        if not [l for l in licenses if l.licenseKey == license_key]:
            raise VMwareObjectRetrievalError('License \'{0}\' wasn\'t found'
                                             ''.format(license_name))
    salt.utils.vmware.assign_license(
        service_instance,
        license_key,
        license_name,
        entity_ref=_get_entity(service_instance, entity),
        entity_name=entity_display_name)