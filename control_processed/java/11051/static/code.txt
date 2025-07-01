private URL tryToResolveRedirects(URL base, String authorization) {
        try {
            HttpURLConnection con = (HttpURLConnection) base.openConnection();
            if (authorization != null) {
                con.addRequestProperty("Authorization", authorization);
            }
            con.getInputStream().close();
            base = con.getURL();
        } catch (Exception ex) {
            // Do not obscure the problem propagating the exception. If the problem is real it will manifest during the
            // actual exchange so will be reported properly there. If it is not real (no permission in UI but sufficient
            // for CLI connection using one of its mechanisms), there is no reason to bother user about it.
            LOGGER.log(Level.FINE, "Failed to resolve potential redirects", ex);
        }
        return base;
    }