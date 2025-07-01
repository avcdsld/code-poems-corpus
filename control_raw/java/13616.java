@GetMapping("/sp/idp/metadata")
    public ResponseEntity<String> getFirstIdentityProviderMetadata() {
        val saml2Client = builtClients.findClient(SAML2Client.class);
        if (saml2Client != null) {
            return getSaml2ClientIdentityProviderMetadataResponseEntity(saml2Client);
        }
        return getNotAcceptableResponseEntity();
    }