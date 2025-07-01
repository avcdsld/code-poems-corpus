def create_volume(name, bricks, stripe=False, replica=False, device_vg=False,
                  transport='tcp', start=False, force=False, arbiter=False):
    '''
    Create a glusterfs volume

    name
        Name of the gluster volume

    bricks
        Bricks to create volume from, in <peer>:<brick path> format. For \
        multiple bricks use list format: '["<peer1>:<brick1>", \
        "<peer2>:<brick2>"]'

    stripe
        Stripe count, the number of bricks should be a multiple of the stripe \
        count for a distributed striped volume

    replica
        Replica count, the number of bricks should be a multiple of the \
        replica count for a distributed replicated volume

    arbiter
        If true, specifies volume should use arbiter brick(s). \
        Valid configuration limited to "replica 3 arbiter 1" per \
        Gluster documentation. Every third brick in the brick list \
        is used as an arbiter brick.

        .. versionadded:: 2019.2.0

    device_vg
        If true, specifies volume should use block backend instead of regular \
        posix backend. Block device backend volume does not support multiple \
        bricks

    transport
        Transport protocol to use, can be 'tcp', 'rdma' or 'tcp,rdma'

    start
        Start the volume after creation

    force
        Force volume creation, this works even if creating in root FS

    CLI Examples:

    .. code-block:: bash

        salt host1 glusterfs.create newvolume host1:/brick

        salt gluster1 glusterfs.create vol2 '["gluster1:/export/vol2/brick", \
        "gluster2:/export/vol2/brick"]' replica=2 start=True
    '''
    # If single brick given as a string, accept it
    if isinstance(bricks, six.string_types):
        bricks = [bricks]

    # Error for block devices with multiple bricks
    if device_vg and len(bricks) > 1:
        raise SaltInvocationError('Block device backend volume does not ' +
                                  'support multiple bricks')

    # Validate bricks syntax
    for brick in bricks:
        try:
            peer_name, path = brick.split(':')
            if not path.startswith('/'):
                raise SaltInvocationError(
                    'Brick paths must start with / in {0}'.format(brick))
        except ValueError:
            raise SaltInvocationError(
                'Brick syntax is <peer>:<path> got {0}'.format(brick))

    # Validate arbiter config
    if arbiter and replica != 3:
        raise SaltInvocationError('Arbiter configuration only valid ' +
                                  'in replica 3 volume')

    # Format creation call
    cmd = 'volume create {0} '.format(name)
    if stripe:
        cmd += 'stripe {0} '.format(stripe)
    if replica:
        cmd += 'replica {0} '.format(replica)
    if arbiter:
        cmd += 'arbiter 1 '
    if device_vg:
        cmd += 'device vg '
    if transport != 'tcp':
        cmd += 'transport {0} '.format(transport)
    cmd += ' '.join(bricks)
    if force:
        cmd += ' force'

    if not _gluster(cmd):
        return False

    if start:
        return start_volume(name)
    return True