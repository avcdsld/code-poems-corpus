public ConfigBuilder<T> withUnsafe(Property<?> property, Object value) {
        String key = String.format("%s.%s", this.namespace, property.getName());
        this.properties.setProperty(key, value.toString());
        return this;
    }