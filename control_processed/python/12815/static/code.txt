def create_ssh_sftp_client(host_ip, port, username, password):
    '''create ssh client'''
    try:
        check_environment()
        import paramiko
        conn = paramiko.Transport(host_ip, port)
        conn.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(conn)
        return sftp
    except Exception as exception:
        print_error('Create ssh client error %s\n' % exception)