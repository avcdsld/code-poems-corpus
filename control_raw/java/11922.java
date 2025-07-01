private String createZfsFileSystem(final TaskListener listener, String rootUsername, String rootPassword) throws IOException, InterruptedException, ZFSException {
        // capture the UID that Hudson runs under
        // so that we can allow this user to do everything on this new partition
        final int uid = LIBC.geteuid();
        final int gid = LIBC.getegid();
        passwd pwd = LIBC.getpwuid(uid);
        if(pwd==null)
            throw new IOException("Failed to obtain the current user information for "+uid);
        final String userName = pwd.pw_name;

        final File home = Jenkins.getInstance().getRootDir();

        // this is the actual creation of the file system.
        // return true indicating a success
        return SU.execute(listener, rootUsername, rootPassword, new Create(listener, home, uid, gid, userName));
    }