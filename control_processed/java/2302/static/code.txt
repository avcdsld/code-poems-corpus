public static <T> ChannelOption<T> of(java.net.SocketOption<T> option) {
        return new NioChannelOption<T>(option);
    }