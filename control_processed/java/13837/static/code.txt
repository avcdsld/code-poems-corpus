protected void createLogoutViewState(final Flow flow) {
        val logoutView = createEndState(flow, CasWebflowConstants.STATE_ID_LOGOUT_VIEW, "casLogoutView");
        logoutView.getEntryActionList().add(createEvaluateAction(CasWebflowConstants.ACTION_ID_LOGOUT_VIEW_SETUP));
    }