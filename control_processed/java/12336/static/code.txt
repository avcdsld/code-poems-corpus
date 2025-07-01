@Restricted(NoExternalUse.class)
    @RestrictedSince("2.37")
    @Deprecated
    public FormValidation doCheckURIEncoding(StaplerRequest request) throws IOException {
        return ExtensionList.lookupSingleton(URICheckEncodingMonitor.class).doCheckURIEncoding(request);
    }