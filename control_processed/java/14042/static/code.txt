protected void updateTicketGrantingTicketState() {
        val ticketGrantingTicket = getTicketGrantingTicket();
        if (ticketGrantingTicket != null && !ticketGrantingTicket.isExpired()) {
            val state = TicketState.class.cast(ticketGrantingTicket);
            state.update();
        }
    }