public static void reportOpenTransactions(String scope, String streamName, int ongoingTransactions) {
        DYNAMIC_LOGGER.reportGaugeValue(OPEN_TRANSACTIONS, ongoingTransactions, streamTags(scope, streamName));
    }