def put_str(content, path, share='C$', conn=None, host=None, username=None, password=None):
    '''
    Wrapper around impacket.smbconnection.putFile() that allows a string to be
    uploaded, without first writing it as a local file
    '''
    if HAS_SMBPROTOCOL:
        return _put_str_smbprotocol(
            content, path, share, conn=conn, host=host,
            username=username, password=password
        )
    elif HAS_IMPACKET:
        return _put_str_impacket(
            content, path, share, conn=conn, host=host, username=username, password=password
        )
    raise MissingSmb("SMB library required (impacket or smbprotocol)")