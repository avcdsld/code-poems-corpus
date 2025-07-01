@Override
    protected boolean isTokenExpired(long tokenExpiryTimeMs) {
        long nowMs = System.currentTimeMillis();
        long maxExpirationMs = TimeUnit.SECONDS.toMillis(tokenValiditySeconds) + nowMs;
        if(!SKIP_TOO_FAR_EXPIRATION_DATE_CHECK && tokenExpiryTimeMs > maxExpirationMs){
            // attempt to use a cookie that has more than the maximum allowed expiration duration
            // was either created before a change of configuration or maliciously crafted
            long diffMs = tokenExpiryTimeMs - maxExpirationMs;
            LOGGER.log(Level.WARNING, "Attempt to use a cookie with an expiration duration larger than the one configured (delta of: {0} ms)", diffMs);
            return true;
        }
        // Check it has not expired
        if (tokenExpiryTimeMs < nowMs) {
            return true;
        }
        return false;
    }