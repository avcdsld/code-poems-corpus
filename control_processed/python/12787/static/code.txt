def kill_command(pid):
    '''kill command'''
    if sys.platform == 'win32':
        process = psutil.Process(pid=pid)
        process.send_signal(signal.CTRL_BREAK_EVENT)
    else:
        cmds = ['kill', str(pid)]
        call(cmds)