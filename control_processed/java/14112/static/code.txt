@Override
    public TransientSessionTicket create(final Service service, final Map<String, Serializable> properties) {
        val id = ticketIdGenerator.getNewTicketId("CAS");
        return new TransientSessionTicketImpl(id, expirationPolicy, service, properties);
    }