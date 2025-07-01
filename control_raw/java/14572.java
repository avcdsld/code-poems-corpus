protected OAuth20TokenGeneratedResult generateAccessTokenOAuthDeviceCodeResponseType(final AccessTokenRequestDataHolder holder) {
        val deviceCode = holder.getDeviceCode();

        if (StringUtils.isNotBlank(deviceCode)) {
            val deviceCodeTicket = getDeviceTokenFromTicketRegistry(deviceCode);
            val deviceUserCode = getDeviceUserCodeFromRegistry(deviceCodeTicket);

            if (deviceUserCode.isUserCodeApproved()) {
                LOGGER.debug("Provided user code [{}] linked to device code [{}] is approved", deviceCodeTicket.getId(), deviceCode);
                this.ticketRegistry.deleteTicket(deviceCode);

                val deviceResult = AccessTokenRequestDataHolder.builder()
                    .service(holder.getService())
                    .authentication(holder.getAuthentication())
                    .registeredService(holder.getRegisteredService())
                    .ticketGrantingTicket(holder.getTicketGrantingTicket())
                    .grantType(holder.getGrantType())
                    .scopes(new LinkedHashSet<>())
                    .responseType(holder.getResponseType())
                    .generateRefreshToken(holder.getRegisteredService() != null && holder.isGenerateRefreshToken())
                    .build();

                val ticketPair = generateAccessTokenOAuthGrantTypes(deviceResult);
                return generateAccessTokenResult(deviceResult, ticketPair);
            }

            if (deviceCodeTicket.getLastTimeUsed() != null) {
                val interval = Beans.newDuration(casProperties.getAuthn().getOauth().getDeviceToken().getRefreshInterval()).getSeconds();
                val shouldSlowDown = deviceCodeTicket.getLastTimeUsed().plusSeconds(interval).isAfter(ZonedDateTime.now(ZoneOffset.UTC));
                if (shouldSlowDown) {
                    LOGGER.error("Request for user code approval is greater than the configured refresh interval of [{}] second(s)", interval);
                    throw new ThrottledOAuth20DeviceUserCodeApprovalException(deviceCodeTicket.getId());
                }
            }
            deviceCodeTicket.update();
            this.ticketRegistry.updateTicket(deviceCodeTicket);
            LOGGER.error("Provided user code [{}] linked to device code [{}] is NOT approved yet", deviceCodeTicket.getId(), deviceCode);
            throw new UnapprovedOAuth20DeviceUserCodeException(deviceCodeTicket.getId());
        }

        val deviceTokens = createDeviceTokensInTicketRegistry(holder);
        return OAuth20TokenGeneratedResult.builder()
            .responseType(holder.getResponseType())
            .registeredService(holder.getRegisteredService())
            .deviceCode(deviceTokens.getLeft().getId())
            .userCode(deviceTokens.getValue().getId())
            .build();
    }