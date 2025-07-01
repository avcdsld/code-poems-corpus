public void trackRequest(String requestDescriptor, long requestId) {
        Preconditions.checkNotNull(requestDescriptor, "Attempting to track a null request descriptor.");
        if (!tracingEnabled) {
            return;
        }

        synchronized (lock) {
            List<Long> requestIds = ongoingRequests.getIfPresent(requestDescriptor);
            if (requestIds == null) {
                requestIds = Collections.synchronizedList(new ArrayList<>());
            }

            requestIds.add(requestId);
            ongoingRequests.put(requestDescriptor, requestIds);
        }

        log.debug("Tracking request {} with id {}.", requestDescriptor, requestId);
    }