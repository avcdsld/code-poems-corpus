protected Collection<Ticket> decodeTickets(final Collection<Ticket> items) {
        return decodeTickets(items.stream()).collect(Collectors.toSet());
    }