def _get_system_volume(vm_):
    '''
    Construct VM system volume list from cloud profile config
    '''

    # Override system volume size if 'disk_size' is defined in cloud profile
    disk_size = get_size(vm_)['disk']
    if 'disk_size' in vm_:
        disk_size = vm_['disk_size']

    # Construct the system volume
    volume = Volume(
        name='{0} Storage'.format(vm_['name']),
        size=disk_size,
        disk_type=get_disk_type(vm_)
    )

    if 'image_password' in vm_:
        image_password = vm_['image_password']
        volume.image_password = image_password

    # Retrieve list of SSH public keys
    ssh_keys = get_public_keys(vm_)
    volume.ssh_keys = ssh_keys

    if 'image_alias' in vm_.keys():
        volume.image_alias = vm_['image_alias']
    else:
        volume.image = get_image(vm_)['id']
        # Set volume availability zone if defined in the cloud profile
        if 'disk_availability_zone' in vm_:
            volume.availability_zone = vm_['disk_availability_zone']

    return volume