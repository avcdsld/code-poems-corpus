private void doReconnect() {
        String interfaceId = consumerConfig.getInterfaceId();
        String appName = consumerConfig.getAppName();
        int thisTime = reconnectFlag.incrementAndGet();
        boolean print = thisTime % 6 == 0; //是否打印error,每6次打印一次
        boolean isAliveEmptyFirst = isAvailableEmpty();
        // 检查可用连接  todo subHealth
        for (Map.Entry<ProviderInfo, ClientTransport> alive : aliveConnections.entrySet()) {
            ClientTransport connection = alive.getValue();
            if (connection != null && !connection.isAvailable()) {
                aliveToRetry(alive.getKey(), connection);
            }
        }
        for (Map.Entry<ProviderInfo, ClientTransport> entry : getRetryConnections()
            .entrySet()) {
            ProviderInfo providerInfo = entry.getKey();
            int providerPeriodCoefficient = CommonUtils.parseNum((Integer)
                providerInfo.getDynamicAttr(ProviderInfoAttrs.ATTR_RC_PERIOD_COEFFICIENT), 1);
            if (thisTime % providerPeriodCoefficient != 0) {
                continue; // 如果命中重连周期，则进行重连
            }
            ClientTransport transport = entry.getValue();
            if (LOGGER.isDebugEnabled(appName)) {
                LOGGER.debugWithApp(appName, "Retry connect to {} provider:{} ...", interfaceId, providerInfo);
            }
            try {
                transport.connect();
                if (doubleCheck(interfaceId, providerInfo, transport)) {
                    providerInfo.setDynamicAttr(ProviderInfoAttrs.ATTR_RC_PERIOD_COEFFICIENT, 1);
                    retryToAlive(providerInfo, transport);
                }
            } catch (Exception e) {
                if (print) {
                    if (LOGGER.isWarnEnabled(appName)) {
                        LOGGER.warnWithApp(appName, "Retry connect to {} provider:{} error ! The exception is " + e
                            .getMessage(), interfaceId, providerInfo);
                    }
                } else {
                    if (LOGGER.isDebugEnabled(appName)) {
                        LOGGER.debugWithApp(appName, "Retry connect to {} provider:{} error ! The exception is " + e
                            .getMessage(), interfaceId, providerInfo);
                    }
                }
            }
        }
        if (isAliveEmptyFirst && !isAvailableEmpty()) { // 原来空，变成不空
            notifyStateChangeToAvailable();
        }
    }