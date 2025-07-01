def check_inheritance(path, objectType, user=None):
    '''
    Check a specified path to verify if inheritance is enabled

    Args:
        path: path of the registry key or file system object to check
        objectType: The type of object (FILE, DIRECTORY, REGISTRY)
        user: if provided, will consider only the ACEs for that user

    Returns (bool): 'Inheritance' of True/False

    CLI Example:

    .. code-block:: bash

        salt 'minion-id' win_dacl.check_inheritance c:\temp directory <username>
    '''

    ret = {'result': False,
           'Inheritance': False,
           'comment': ''}

    sidRet = _getUserSid(user)

    dc = daclConstants()
    objectType = dc.getObjectTypeBit(objectType)
    path = dc.processPath(path, objectType)

    try:
        sd = win32security.GetNamedSecurityInfo(path, objectType, win32security.DACL_SECURITY_INFORMATION)
        dacls = sd.GetSecurityDescriptorDacl()
    except Exception as e:
        ret['result'] = False
        ret['comment'] = 'Error obtaining the Security Descriptor or DACL of the path: {0}.'.format(e)
        return ret

    for counter in range(0, dacls.GetAceCount()):
        ace = dacls.GetAce(counter)
        if (ace[0][1] & win32security.INHERITED_ACE) == win32security.INHERITED_ACE:
            if not sidRet['sid'] or ace[2] == sidRet['sid']:
                ret['Inheritance'] = True
                break

    ret['result'] = True
    return ret