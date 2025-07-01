protected void createTicketGrantingTicketCheckAction(final Flow flow) {
        val action = createActionState(flow, CasWebflowConstants.STATE_ID_TICKET_GRANTING_TICKET_CHECK,
            CasWebflowConstants.ACTION_ID_TICKET_GRANTING_TICKET_CHECK);
        createTransitionForState(action, CasWebflowConstants.TRANSITION_ID_TGT_NOT_EXISTS, CasWebflowConstants.STATE_ID_GATEWAY_REQUEST_CHECK);
        createTransitionForState(action, CasWebflowConstants.TRANSITION_ID_TGT_INVALID, CasWebflowConstants.STATE_ID_TERMINATE_SESSION);
        createTransitionForState(action, CasWebflowConstants.TRANSITION_ID_TGT_VALID, CasWebflowConstants.STATE_ID_HAS_SERVICE_CHECK);
    }