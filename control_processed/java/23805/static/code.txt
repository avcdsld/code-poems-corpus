public ExtensionClass<T> getExtensionClass(String alias) {
        return all == null ? null : all.get(alias);
    }