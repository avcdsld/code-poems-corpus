protected RoleDescriptorResolver getRoleDescriptorResolver(final MetadataResolver resolver,
                                                               final MessageContext context,
                                                               final RequestAbstractType profileRequest) throws Exception {
        val idp = casProperties.getAuthn().getSamlIdp();
        return SamlIdPUtils.getRoleDescriptorResolver(resolver, idp.getMetadata().isRequireValidMetadata());
    }