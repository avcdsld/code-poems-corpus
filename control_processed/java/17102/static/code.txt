public static void setDaemonizedThreadFactories(MediaDriver.Context mediaDriverCtx){

        //Set thread factories so we can make the Aeron threads daemon threads (some are not by default)
        mediaDriverCtx.conductorThreadFactory(r -> {
            Thread t = new Thread(r);
            t.setDaemon(true);
            t.setName("aeron-conductor-thread-" + conductorCount.getAndIncrement());
            return t;
        });

        mediaDriverCtx.receiverThreadFactory(r -> {
            Thread t = new Thread(r);
            t.setDaemon(true);
            t.setName("aeron-receiver-thread-" + receiverCount.getAndIncrement());
            return t;
        });


        mediaDriverCtx.senderThreadFactory(r -> {
            Thread t = new Thread(r);
            t.setDaemon(true);
            t.setName("aeron-sender-thread-" + senderCount.getAndIncrement());
            return t;
        });


        mediaDriverCtx.sharedNetworkThreadFactory(r -> {
            Thread t = new Thread(r);
            t.setDaemon(true);
            t.setName("aeron-shared-network-thread-" + sharedNetworkCount.getAndIncrement());
            return t;
        });

        mediaDriverCtx.sharedThreadFactory(r -> {
            Thread t = new Thread(r);
            t.setDaemon(true);
            t.setName("aeron-shared-thread-" + sharedThreadCount.getAndIncrement());
            return t;
        });
    }