@Override
    public Channel getChannelOrFail() throws ChannelClosedException {
        final Channel ch = Channel.current();
        if (ch == null) {
            throw new ChannelClosedException(new IllegalStateException("No channel associated with the thread"));
        }
        return ch;
    }