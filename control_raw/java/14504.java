protected void createServiceAuthorizationCheckAction(final Flow flow) {
        val serviceAuthorizationCheck = createActionState(flow,
            CasWebflowConstants.STATE_ID_SERVICE_AUTHZ_CHECK, "serviceAuthorizationCheck");
        createStateDefaultTransition(serviceAuthorizationCheck, CasWebflowConstants.STATE_ID_INIT_LOGIN_FORM);
    }