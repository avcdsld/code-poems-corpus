@JavaScriptMethod public final JSONObject news() {
        lastNewsTime = System.currentTimeMillis();
        JSONObject r = new JSONObject();
        try {
            r.put("data", data());
        } catch (RuntimeException x) {
            LOG.log(Level.WARNING, "failed to update " + uri, x);
            status = ERROR;
        }
        Object statusJSON = status == 1 ? "done" : status == CANCELED ? "canceled" : status == ERROR ? "error" : status;
        r.put("status", statusJSON);
        if (statusJSON instanceof String) { // somehow completed
            LOG.log(Level.FINE, "finished in news so releasing {0}", boundId);
            release();
        }
        lastNewsTime = System.currentTimeMillis();
        LOG.log(Level.FINER, "news from {0}", uri);
        return r;
    }