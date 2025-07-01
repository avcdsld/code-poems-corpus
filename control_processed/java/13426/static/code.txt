public String getPrincipalAttributeValue(final Principal p, final String attributeName) {
        val attributes = p.getAttributes();
        if (attributes.containsKey(attributeName)) {
            return CollectionUtils.toCollection(attributes.get(attributeName)).iterator().next().toString();
        }
        return null;
    }