def reset_time(path='.', amt=None):
    '''
    Reset atime/mtime on all files to prevent systemd swipes only part of the files in the /tmp.
    '''
    if not amt:
        amt = int(time.time())
    for fname in os.listdir(path):
        fname = os.path.join(path, fname)
        if os.path.isdir(fname):
            reset_time(fname, amt=amt)
        os.utime(fname, (amt, amt,))