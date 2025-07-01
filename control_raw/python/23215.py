def runas_unpriv(cmd, username, password, cwd=None):
    '''
    Runas that works for non-priviledged users
    '''
    # Create a pipe to set as stdout in the child. The write handle needs to be
    # inheritable.
    c2pread, c2pwrite = salt.platform.win.CreatePipe(
        inherit_read=False, inherit_write=True,
    )
    errread, errwrite = salt.platform.win.CreatePipe(
        inherit_read=False, inherit_write=True,
    )

    # Create inheritable copy of the stdin
    stdin = salt.platform.win.kernel32.GetStdHandle(
            salt.platform.win.STD_INPUT_HANDLE,
    )
    dupin = salt.platform.win.DuplicateHandle(srchandle=stdin, inherit=True)

    # Get startup info structure
    startup_info = salt.platform.win.STARTUPINFO(
        dwFlags=win32con.STARTF_USESTDHANDLES,
        hStdInput=dupin,
        hStdOutput=c2pwrite,
        hStdError=errwrite,
    )

    username, domain = split_username(username)

    # Run command and return process info structure
    process_info = salt.platform.win.CreateProcessWithLogonW(
            username=username,
            domain=domain,
            password=password,
            logonflags=salt.platform.win.LOGON_WITH_PROFILE,
            commandline=cmd,
            startupinfo=startup_info,
            currentdirectory=cwd)

    salt.platform.win.kernel32.CloseHandle(dupin)
    salt.platform.win.kernel32.CloseHandle(c2pwrite)
    salt.platform.win.kernel32.CloseHandle(errwrite)
    salt.platform.win.kernel32.CloseHandle(process_info.hThread)

    # Initialize ret and set first element
    ret = {'pid': process_info.dwProcessId}

    # Get Standard Out
    fd_out = msvcrt.open_osfhandle(c2pread, os.O_RDONLY | os.O_TEXT)
    with os.fdopen(fd_out, 'r') as f_out:
        ret['stdout'] = f_out.read()

    # Get Standard Error
    fd_err = msvcrt.open_osfhandle(errread, os.O_RDONLY | os.O_TEXT)
    with os.fdopen(fd_err, 'r') as f_err:
        ret['stderr'] = f_err.read()

    # Get Return Code
    if salt.platform.win.kernel32.WaitForSingleObject(process_info.hProcess, win32event.INFINITE) == \
            win32con.WAIT_OBJECT_0:
        exitcode = salt.platform.win.wintypes.DWORD()
        salt.platform.win.kernel32.GetExitCodeProcess(process_info.hProcess,
                                    ctypes.byref(exitcode))
        ret['retcode'] = exitcode.value

    # Close handle to process
    salt.platform.win.kernel32.CloseHandle(process_info.hProcess)

    return ret