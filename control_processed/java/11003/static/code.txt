protected final boolean canceled() {
        if (DEBUG_SLEEP != null) {
            try {
                Thread.sleep(DEBUG_SLEEP);
            } catch (InterruptedException x) {}
        }
        if (status == ERROR) {
            return true; // recent call to data() failed
        }
        long now = System.currentTimeMillis();
        long elapsed = now - lastNewsTime;
        if (elapsed > timeout()) {
            status = CANCELED;
            LOG.log(Level.FINE, "{0} canceled due to {1}msec inactivity after {2}msec", new Object[] {uri, elapsed, now - start});
            return true;
        } else {
            return false;
        }
    }