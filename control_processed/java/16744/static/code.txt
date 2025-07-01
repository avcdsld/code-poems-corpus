@Override
    public void updateState(SubscriberState subscriberState) {
        updated.put(subscriberState.getStreamId(), System.currentTimeMillis());
        statusStorageMap.put(subscriberState.getStreamId(), subscriberState);
    }