private void mkDir(String dir) throws Exception {
        Session session = getSession();
        session.connect();
        Channel channel = session.openChannel("sftp");
        channel.connect();

        ChannelSftp c = (ChannelSftp) channel;
        if (!fileExists(dir, c))
            c.mkdir(dir);
        c.exit();
        session.disconnect();
    }