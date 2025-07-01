protected void clientMessageHandler(DirectBuffer buffer, int offset, int length, Header header) {
        /**
         *  All incoming messages here are supposed to be "just messages", only unicast communication
         *  All of them should implement MeaningfulMessage interface
         */
        // TODO: to be implemented
        //  log.info("clientMessageHandler message request incoming");

        byte[] data = new byte[length];
        buffer.getBytes(offset, data);

        MeaningfulMessage message = (MeaningfulMessage) VoidMessage.fromBytes(data);
        completed.put(message.getTaskId(), message);
    }