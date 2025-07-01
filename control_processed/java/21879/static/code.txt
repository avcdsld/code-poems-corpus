@Override
    public void run() {

        while (!registered) {
                GetOperationRequest operationRequest = new GetOperationRequest().withOperationId(operationId);
                GetOperationResult result = discoveryClient.getOperation(operationRequest);
                if (LOG.isInfoEnabled()) {
                    LOG.info("Service registration for operation " + operationId + " resulted in " + result.getOperation().getStatus());
                }
                if (result.getOperation().getStatus().equalsIgnoreCase("failure") || result.getOperation().getStatus().equalsIgnoreCase("success")) {
                    registered = true; // either way we are done
                    if (result.getOperation().getStatus().equalsIgnoreCase("failure")) {
                        if (route53AutoRegistrationConfiguration.isFailFast() && embeddedServerInstance instanceof EmbeddedServerInstance) {
                            if (LOG.isErrorEnabled()) {
                                LOG.error("Error registering instance shutting down instance because failfast is set.");
                            }
                            ((EmbeddedServerInstance) embeddedServerInstance).getEmbeddedServer().stop();
                        }
                    }
                }
            }
            try {
                Thread.currentThread().sleep(5000);
            } catch (InterruptedException e) {
                if (LOG.isErrorEnabled()) {
                    LOG.error("Registration monitor service has been aborted, unable to verify proper service registration on Route 53.", e);
                }
            }
        }