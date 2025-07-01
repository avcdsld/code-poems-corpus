private void acceptAttributes(Collection<AttributeUpdate> attributeUpdates) {
        if (attributeUpdates == null) {
            return;
        }

        for (AttributeUpdate au : attributeUpdates) {
            this.attributeUpdates.put(au.getAttributeId(), au.getValue());
        }
    }