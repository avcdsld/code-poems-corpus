@Override
    public void close() throws Exception {
        if (subscriber != null) {
            for (int i = 0; i < subscriber.length; i++) {
                if (subscriber[i] != null) {
                    subscriber[i].close();
                }
            }
        }
        if (server != null)
            server.stop();
        if (mediaDriver != null)
            CloseHelper.quietClose(mediaDriver);
        if (aeron != null)
            CloseHelper.quietClose(aeron);

    }