public static int findAvailableTcpPort(int minPortRange, int maxPortRange) {
        ArgumentUtils.check(() -> minPortRange > MIN_PORT_RANGE)
            .orElseFail("Port minimum value must be greater than " + MIN_PORT_RANGE);
        ArgumentUtils.check(() -> maxPortRange >= minPortRange)
            .orElseFail("Max port range must be greater than minimum port range");
        ArgumentUtils.check(() -> maxPortRange <= MAX_PORT_RANGE)
            .orElseFail("Port maximum value must be less than " + MAX_PORT_RANGE);

        int currentPort = nextPort(minPortRange, maxPortRange);
        while (!isTcpPortAvailable(currentPort)) {
            currentPort = nextPort(minPortRange, maxPortRange);
        }
        return currentPort;
    }