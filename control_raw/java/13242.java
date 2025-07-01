@SneakyThrows
    protected Ticket encodeTicket(final Ticket ticket) {
        if (!isCipherExecutorEnabled()) {
            LOGGER.trace(MESSAGE);
            return ticket;
        }
        if (ticket == null) {
            LOGGER.debug("Ticket passed is null and cannot be encoded");
            return null;
        }
        LOGGER.debug("Encoding ticket [{}]", ticket);
        val encodedTicketObject = SerializationUtils.serializeAndEncodeObject(this.cipherExecutor, ticket);
        val encodedTicketId = encodeTicketId(ticket.getId());
        val encodedTicket = new EncodedTicket(encodedTicketId, ByteSource.wrap(encodedTicketObject).read());
        LOGGER.debug("Created encoded ticket [{}]", encodedTicket);
        return encodedTicket;
    }