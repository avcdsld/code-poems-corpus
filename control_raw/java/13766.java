protected boolean sendMessageToEndpoint(final LogoutHttpMessage msg, final SingleLogoutRequest request, final SingleLogoutMessage logoutMessage) {
        return this.httpClient.sendMessageToEndPoint(msg);
    }