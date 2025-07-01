def pull_tar(url, name, verify=False):
    '''
    Execute a ``machinectl pull-raw`` to download a .tar container image,
    and add it to /var/lib/machines as a new container.

    .. note::

        **Requires systemd >= 219**

    url
        URL from which to download the container

    name
        Name for the new container

    verify : False
        Perform signature or checksum verification on the container. See the
        ``machinectl(1)`` man page (section titled "Image Transfer Commands")
        for more information on requirements for image verification. To perform
        signature verification, use ``verify=signature``. For checksum
        verification, use ``verify=checksum``. By default, no verification will
        be performed.

    CLI Examples:

    .. code-block:: bash

        salt myminion nspawn.pull_tar http://foo.domain.tld/containers/archlinux-2015.02.01.tar.gz arch2
    '''
    return _pull_image('tar', url, name, verify=verify)