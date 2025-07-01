def resource_present(name, resource_id, resource_type, resource_options=None, cibname=None):
    '''
    Ensure that a resource is created

    Should be run on one cluster node only
    (there may be races)
    Can only be run on a node with a functional pacemaker/corosync

    name
        Irrelevant, not used (recommended: {{formulaname}}__resource_present_{{resource_id}})
    resource_id
        name for the resource
    resource_type
        resource type (f.e. ocf:heartbeat:IPaddr2 or VirtualIP)
    resource_options
        additional options for creating the resource
    cibname
        use a cached CIB-file named like cibname instead of the live CIB

    Example:

    .. code-block:: yaml

        mysql_pcs__resource_present_galera:
            pcs.resource_present:
                - resource_id: galera
                - resource_type: "ocf:heartbeat:galera"
                - resource_options:
                    - 'wsrep_cluster_address=gcomm://node1.example.org,node2.example.org,node3.example.org'
                    - '--master'
                - cibname: cib_for_galera
    '''
    return _item_present(name=name,
                         item='resource',
                         item_id=resource_id,
                         item_type=resource_type,
                         extra_args=resource_options,
                         cibname=cibname)