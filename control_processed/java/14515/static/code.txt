protected void createWarnDecisionState(final Flow flow) {
        createDecisionState(flow, CasWebflowConstants.STATE_ID_WARN,
            "flowScope.warnCookieValue",
            CasWebflowConstants.STATE_ID_SHOW_WARNING_VIEW,
            CasWebflowConstants.STATE_ID_REDIRECT);
    }