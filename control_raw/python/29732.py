def resource_defaults_to(name, default, value, extra_args=None, cibname=None):
    '''
    Ensure a resource default in the cluster is set to a given value

    Should be run on one cluster node only
    (there may be races)
    Can only be run on a node with a functional pacemaker/corosync

    name
        Irrelevant, not used (recommended: pcs_properties__resource_defaults_to_{{default}})
    default
        name of the default resource property
    value
        value of the default resource property
    extra_args
        additional options for the pcs command
    cibname
        use a cached CIB-file named like cibname instead of the live CIB

    Example:

    .. code-block:: yaml

        pcs_properties__resource_defaults_to_resource-stickiness:
            pcs.resource_defaults_to:
                - default: resource-stickiness
                - value: 100
                - cibname: cib_for_cluster_settings
    '''
    return _item_present(name=name,
                         item='resource',
                         item_id='{0}={1}'.format(default, value),
                         item_type=None,
                         show='defaults',
                         create='defaults',
                         extra_args=extra_args,
                         cibname=cibname)