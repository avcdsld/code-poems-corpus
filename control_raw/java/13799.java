@Override
    public Map<String, List<Object>> filter(final Map<String, List<Object>> givenAttributes) {
        val attributesToRelease = new HashMap<String, List<Object>>();
        givenAttributes.entrySet()
            .stream()
            .filter(entry -> {
                val attributeName = entry.getKey();
                val attributeValue = entry.getValue();
                LOGGER.debug("Received attribute [{}] with value [{}]", attributeName, attributeValue);
                return attributeValue != null;
            })
            .forEach(entry -> {
                val attributeName = entry.getKey();
                val attributeValue = entry.getValue();
                LOGGER.trace("Attribute value [{}] is a collection", attributeValue);
                val filteredAttributes = filterAttributes(attributeValue, attributeName);
                if (!filteredAttributes.isEmpty()) {
                    attributesToRelease.put(attributeName, filteredAttributes);
                }
            });
        LOGGER.debug("Received [{}] attributes. Filtered and released [{}]", givenAttributes.size(), attributesToRelease.size());
        return attributesToRelease;
    }