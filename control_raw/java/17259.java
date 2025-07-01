public void setIfUnset(String name, String value) {
        if (get(name) == null) {
            set(name, value);
        }
    }