def member_present(ip, port, balancer_id, profile, **libcloud_kwargs):
    '''
    Ensure a load balancer member is present

    :param ip: IP address for the new member
    :type  ip: ``str``

    :param port: Port for the new member
    :type  port: ``int``

    :param balancer_id: id of a load balancer you want to attach the member to
    :type  balancer_id: ``str``

    :param profile: The profile key
    :type  profile: ``str``
    '''
    existing_members = __salt__['libcloud_loadbalancer.list_balancer_members'](balancer_id, profile)
    for member in existing_members:
        if member['ip'] == ip and member['port'] == port:
            return state_result(True, "Member already present", balancer_id)
    member = __salt__['libcloud_loadbalancer.balancer_attach_member'](balancer_id, ip, port, profile, **libcloud_kwargs)
    return state_result(True, "Member added to balancer, id: {0}".format(member['id']), balancer_id, member)