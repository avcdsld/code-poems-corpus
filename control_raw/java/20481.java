protected void performActions(List<HttpMessage> httpMessages) {
        for (HttpMessage httpMessage : httpMessages) {
            if (httpMessage != null) {
                performAction(httpMessage);
            }
        }
    }