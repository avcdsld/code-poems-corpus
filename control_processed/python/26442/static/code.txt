def vm_cputime(vm_=None):
    '''
    Return cputime used by the vms on this hyper in a
    list of dicts:

    .. code-block:: python

        [
            'your-vm': {
                'cputime' <int>
                'cputime_percent' <int>
                },
            ...
            ]

    If you pass a VM name in as an argument then it will return info
    for just the named VM, otherwise it will return all VMs.

    CLI Example:

    .. code-block:: bash

        salt '*' virt.vm_cputime
    '''
    with _get_xapi_session() as xapi:
        def _info(vm_):
            host_rec = _get_record_by_label(xapi, 'VM', vm_)
            host_cpus = len(host_rec['host_CPUs'])
            if host_rec is False:
                return False
            host_metrics = _get_metrics_record(xapi, 'VM', host_rec)
            vcpus = int(host_metrics['VCPUs_number'])
            cputime = int(host_metrics['VCPUs_utilisation']['0'])
            cputime_percent = 0
            if cputime:
                # Divide by vcpus to always return a number between 0 and 100
                cputime_percent = (1.0e-7 * cputime / host_cpus) / vcpus
            return {'cputime': int(cputime),
                    'cputime_percent': int('{0:.0f}'.format(cputime_percent))}
        info = {}
        if vm_:
            info[vm_] = _info(vm_)
            return info

        for vm_ in list_domains():
            info[vm_] = _info(vm_)

        return info