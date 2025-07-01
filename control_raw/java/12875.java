public static MessageHandler signallingMessageHandler(final ProcessEngine processEngine) {
        return new MessageHandler() {
            @Override
            public void handleMessage(Message<?> message) throws MessagingException {
                String executionId = message.getHeaders().containsKey("executionId") ?
                        (String) message.getHeaders().get("executionId") : (String) null;

                if (null != executionId)
                    processEngine.getRuntimeService().trigger(executionId);
            }
        };
    }