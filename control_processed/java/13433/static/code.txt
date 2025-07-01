protected boolean doRejectedAttributesRefusePrincipalAccess(final Map<String, Object> principalAttributes) {
        LOGGER.debug("These rejected attributes [{}] are examined against [{}] before service can proceed.", rejectedAttributes, principalAttributes);
        if (rejectedAttributes.isEmpty()) {
            return false;
        }
        return requiredAttributesFoundInMap(principalAttributes, rejectedAttributes);
    }