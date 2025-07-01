protected boolean ipPatternMatches(final String remoteIp) {
        val matcher = this.ipsToCheckPattern.matcher(remoteIp);
        if (matcher.find()) {
            LOGGER.debug("Remote IP address [{}] should be checked based on the defined pattern [{}]", remoteIp, this.ipsToCheckPattern.pattern());
            return true;
        }
        LOGGER.debug("No pattern or remote IP defined, or pattern does not match remote IP [{}]", remoteIp);
        return false;
    }