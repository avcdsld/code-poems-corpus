def example_alter_configs(a, args):
    """ Alter configs atomically, replacing non-specified
    configuration properties with their default values.
    """

    resources = []
    for restype, resname, configs in zip(args[0::3], args[1::3], args[2::3]):
        resource = ConfigResource(restype, resname)
        resources.append(resource)
        for k, v in [conf.split('=') for conf in configs.split(',')]:
            resource.set_config(k, v)

    fs = a.alter_configs(resources)

    # Wait for operation to finish.
    for res, f in fs.items():
        try:
            f.result()  # empty, but raises exception on failure
            print("{} configuration successfully altered".format(res))
        except Exception:
            raise