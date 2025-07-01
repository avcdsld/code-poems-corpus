public AnnotationValueBuilder<T> member(String name, String... strings) {
        if (strings != null) {
            values.put(name, strings);
        }
        return this;
    }