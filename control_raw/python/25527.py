def container_device_get(name, device_name, remote_addr=None,
                         cert=None, key=None, verify_cert=True):
    '''
    Get a container device

    name :
        Name of the container

    device_name :
        The device name to retrieve

    remote_addr :
        An URL to a remote Server, you also have to give cert and key if
        you provide remote_addr and its a TCP Address!

        Examples:
            https://myserver.lan:8443
            /var/lib/mysocket.sock

    cert :
        PEM Formatted SSL Certificate.

        Examples:
            ~/.config/lxc/client.crt

    key :
        PEM Formatted SSL Key.

        Examples:
            ~/.config/lxc/client.key

    verify_cert : True
        Wherever to verify the cert, this is by default True
        but in the most cases you want to set it off as LXD
        normaly uses self-signed certificates.
    '''
    container = container_get(
        name, remote_addr, cert, key, verify_cert, _raw=True
    )

    return _get_property_dict_item(container, 'devices', device_name)