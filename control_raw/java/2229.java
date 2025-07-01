protected NameResolver<InetAddress> newNameResolver(EventLoop eventLoop,
                                                        ChannelFactory<? extends DatagramChannel> channelFactory,
                                                        DnsServerAddressStreamProvider nameServerProvider)
            throws Exception {
        // once again, channelFactory and nameServerProvider are most probably set in builder already,
        // but I do reassign them again to avoid corner cases with override methods
        return dnsResolverBuilder.eventLoop(eventLoop)
                .channelFactory(channelFactory)
                .nameServerProvider(nameServerProvider)
                .build();
    }