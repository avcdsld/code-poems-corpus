function set(object, path, value) {
        return object == null ? object : baseSet(object, path, value);
    }