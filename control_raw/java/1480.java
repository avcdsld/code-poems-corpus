public EpollServerSocketChannelConfig setFreeBind(boolean freeBind) {
        try {
            ((EpollServerSocketChannel) channel).socket.setIpFreeBind(freeBind);
            return this;
        } catch (IOException e) {
            throw new ChannelException(e);
        }
    }