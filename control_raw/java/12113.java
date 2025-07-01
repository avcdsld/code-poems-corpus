public ArgumentListBuilder addKeyValuePairs(String prefix, Map<String,String> props, Set<String> propsToMask) {
        for (Entry<String,String> e : props.entrySet()) {
            addKeyValuePair(prefix, e.getKey(), e.getValue(), (propsToMask != null) && propsToMask.contains(e.getKey()));
        }
        return this;
    }