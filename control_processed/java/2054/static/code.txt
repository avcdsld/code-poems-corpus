private void updateInitialReceiveWindowSize(int newInitialWindowSize) {
        int deltaWindowSize = newInitialWindowSize - initialReceiveWindowSize;
        initialReceiveWindowSize = newInitialWindowSize;
        spdySession.updateAllReceiveWindowSizes(deltaWindowSize);
    }