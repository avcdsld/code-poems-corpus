protected String encodeTicketId(final String ticketId) {
        if (!isCipherExecutorEnabled()) {
            LOGGER.trace(MESSAGE);
            return ticketId;
        }
        if (StringUtils.isBlank(ticketId)) {
            return ticketId;
        }
        val encodedId = DigestUtils.sha512(ticketId);
        LOGGER.debug("Encoded original ticket id [{}] to [{}]", ticketId, encodedId);
        return encodedId;
    }