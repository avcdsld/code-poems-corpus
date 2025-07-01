public boolean canPing() {
        val uidPsw = getClass().getSimpleName();
        for (val server : this.servers) {
            LOGGER.debug("Attempting to ping RADIUS server [{}] via simulating an authentication request. If the server responds "
                + "successfully, mock authentication will fail correctly.", server);
            try {
                server.authenticate(uidPsw, uidPsw);
            } catch (final TimeoutException | SocketTimeoutException e) {
                LOGGER.debug("Server [{}] is not available", server);
                continue;
            } catch (final Exception e) {
                LOGGER.debug("Pinging RADIUS server was successful. Response [{}]", e.getMessage());
            }
            return true;
        }
        return false;
    }