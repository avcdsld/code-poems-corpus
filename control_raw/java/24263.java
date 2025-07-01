public ProviderInfo setStaticAttr(String staticAttrKey, String staticAttrValue) {
        if (staticAttrValue == null) {
            staticAttrs.remove(staticAttrKey);
        } else {
            staticAttrs.put(staticAttrKey, staticAttrValue);
        }
        return this;
    }