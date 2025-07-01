protected void createRedirectUnauthorizedServiceUrlEndState(final Flow flow) {
        val state = createEndState(flow, CasWebflowConstants.STATE_ID_VIEW_REDIR_UNAUTHZ_URL, "flowScope.unauthorizedRedirectUrl", true);
        state.getEntryActionList().add(createEvaluateAction("redirectUnauthorizedServiceUrlAction"));
    }