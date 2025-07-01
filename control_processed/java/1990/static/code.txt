private int doWriteMultiple(ChannelOutboundBuffer in) throws Exception {
        final long maxBytesPerGatheringWrite = config().getMaxBytesPerGatheringWrite();
        IovArray array = ((KQueueEventLoop) eventLoop()).cleanArray();
        array.maxBytes(maxBytesPerGatheringWrite);
        in.forEachFlushedMessage(array);

        if (array.count() >= 1) {
            // TODO: Handle the case where cnt == 1 specially.
            return writeBytesMultiple(in, array);
        }
        // cnt == 0, which means the outbound buffer contained empty buffers only.
        in.removeBytes(0);
        return 0;
    }