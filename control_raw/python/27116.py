def create_cluster(kwargs=None, call=None):
    '''
    Create a new cluster under the specified datacenter in this VMware environment

    CLI Example:

    .. code-block:: bash

        salt-cloud -f create_cluster my-vmware-config name="myNewCluster" datacenter="datacenterName"
    '''
    if call != 'function':
        raise SaltCloudSystemExit(
            'The create_cluster function must be called with '
            '-f or --function.'
        )

    cluster_name = kwargs.get('name') if kwargs and 'name' in kwargs else None
    datacenter = kwargs.get('datacenter') if kwargs and 'datacenter' in kwargs else None

    if not cluster_name:
        raise SaltCloudSystemExit(
            'You must specify name of the new cluster to be created.'
        )

    if not datacenter:
        raise SaltCloudSystemExit(
            'You must specify name of the datacenter where the cluster should be created.'
        )

    # Get the service instance
    si = _get_si()

    if not isinstance(datacenter, vim.Datacenter):
        datacenter = salt.utils.vmware.get_mor_by_property(si, vim.Datacenter, datacenter)
        if not datacenter:
            raise SaltCloudSystemExit(
                'The specified datacenter does not exist.'
            )

    # Check if cluster already exists
    cluster_ref = salt.utils.vmware.get_mor_by_property(si, vim.ClusterComputeResource, cluster_name)
    if cluster_ref:
        return {cluster_name: 'cluster already exists'}

    cluster_spec = vim.cluster.ConfigSpecEx()
    folder = datacenter.hostFolder

    # Verify that the folder is of type vim.Folder
    if isinstance(folder, vim.Folder):
        try:
            folder.CreateClusterEx(name=cluster_name, spec=cluster_spec)
        except Exception as exc:
            log.error(
                'Error creating cluster %s: %s',
                cluster_name, exc,
                # Show the traceback if the debug logging level is enabled
                exc_info_on_loglevel=logging.DEBUG
            )
            return False

        log.debug(
            "Created cluster %s under datacenter %s",
            cluster_name, datacenter.name
        )
        return {cluster_name: 'created'}

    return False