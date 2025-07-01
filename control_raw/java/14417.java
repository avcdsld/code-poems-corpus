@UpdateHandler(name = "delete_token", file = "CouchDbOneTimeToken_delete.js")
    public void deleteToken(final CouchDbGoogleAuthenticatorToken token) {
        db.callUpdateHandler(stdDesignDocumentId, "delete_token", token.getCid(), null);
    }